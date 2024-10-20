import pytest
from app import create_app
from test_config import TestConfigApp


@pytest.fixture()
def app():
    app = create_app(config=TestConfigApp)
    app.config.update({'TESTING': True})

    # settings app

    yield app

    # clean up app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
