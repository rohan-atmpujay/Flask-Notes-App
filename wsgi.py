from website import create_app
from waitress import serve


app = create_app()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
from website import create_app
from waitress import serve
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
