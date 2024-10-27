import pytest
from app import create_app
from config_test import TestAppConfig


@pytest.fixture()
def app():
    app = create_app(config=TestAppConfig)  # pylint: disable=redefined-outer-name
    app.config.update({'TESTING': True})

    # settings app

    yield app

    # clean up app


@pytest.fixture()
def client(app):  # pylint: disable=redefined-outer-name
    return app.test_client()


@pytest.fixture()
def runner(app):  # pylint: disable=redefined-outer-name
    return app.test_cli_runner()

