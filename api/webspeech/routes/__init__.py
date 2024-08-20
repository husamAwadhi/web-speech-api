from flask import Blueprint

bp = Blueprint("main", __name__)

from webspeech.routes import main  # noqa: E402

__all__ = [
    "main",
]
