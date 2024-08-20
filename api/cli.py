from flask.cli import FlaskGroup
from webspeech import create_app
import os

app = create_app(
    "config.DevConfig"
    if int(os.environ.get("FLASK_DEBUG")) == 1
    else "config.ProdConfig"
)

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
