from flask import Flask, jsonify
from config import Config
from flask_cors import CORS
from werkzeug.exceptions import HTTPException


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, origins=app.config["ORIGINS"])

    from webspeech.routes import bp as main_bp

    app.register_blueprint(main_bp)

    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            return jsonify(error=str(e)), e.code
        return jsonify(error=str(e) if app.debug else "internal server error"), 500

    return app
