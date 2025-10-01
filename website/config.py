import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_key")

    DATABASE_URL = os.environ.get("DATABASE_URL")
    if not DATABASE_URL:

        DATABASE_URL = os.path.join(os.getcwd(), "website.db")

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_URL}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
