from config import get_app_config
from foodie_app import create_app


if __name__ == '__main__':
    app = create_app(get_app_config())
    app.run(host='127.0.0.1', port=5000)
