from flask import Flask

from config import ConfigApp


def create_app(config=ConfigApp):

    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        from app import routes

    return app

