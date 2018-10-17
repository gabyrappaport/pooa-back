from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    from app import itn_bp
    app.register_blueprint(itn_bp, url_prefix='/itn')

    CORS(app, origins="*", allow_headers=[
        "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
         supports_credentials=True)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
