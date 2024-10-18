from flask import Flask

from config import ConfigApp


def create_app(config=ConfigApp):

    app = Flask(__name__)
    app.config.from_object(config)

    from .root import bp
    app.register_blueprint(bp)

    return app
