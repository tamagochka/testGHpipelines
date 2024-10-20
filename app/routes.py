from flask import current_app


@current_app.route('/')
@current_app.route('/index')
def index():
    return 'Hello, World!!!'
