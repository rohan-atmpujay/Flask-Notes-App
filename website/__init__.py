from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Initialize database
db = SQLAlchemy()

# Default DB name (used locally)
LOCAL_DB_NAME = 'website.db'

def create_app():
    app = Flask(__name__)

    # Load config from config.py
    app.config.from_object('website.config.Config')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Use persistent SQLite path if DATABASE_URL env var is not set
    db_path = os.environ.get("DATABASE_URL")
    if not db_path:
        # For local dev or Render persistent storage
        db_path = os.path.join(os.getcwd(), LOCAL_DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

    # Initialize extensions
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Import models after db is initialized to avoid circular imports
    from .models import User, Note

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints
    from .view import views
    from .auth import auth
    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix="/")  # cleaner URL structure

    # Create database if it doesn't exist
    create_database(app, db_path)

    return app

def create_database(app, db_path):
    """Creates the database if it doesn't exist."""
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
        print(f'Database successfully created at {db_path}!')
