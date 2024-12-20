from app import create_app
from config import AppConfig

app = create_app(config=AppConfig)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
