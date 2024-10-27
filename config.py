import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


class AppConfig:  # pylint: disable=too-few-public-methods

    DEBUG = True
    HOST = os.getenv('HOST', 'localhost')
    PORT = os.getenv('PORT', '5000')
