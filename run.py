from app import create_app
from config import ConfigApp

app = create_app(config=ConfigApp)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])


