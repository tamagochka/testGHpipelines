from flask import Flask

from config import AppConfig


def create_app(config=AppConfig):

    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        from app import routes  # pylint: disable=C0415, E0401, W0611

    return app
