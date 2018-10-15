from flask import Flask

def create_app():
    app = Flask(__name__)

    from app import itn_bp
    app.register_blueprint(itn_bp, url_prefix='/itn')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)