from flask import current_app, Blueprint

bp = Blueprint('root', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    return 'Hello, World!!!'
