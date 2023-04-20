from flask import Flask
from dynaconf import FlaskDynaconf


def create_app():
    """
    Create and configure an instance of the Flask application.
    """
    app = Flask(__name__)
    FlaskDynaconf(app, settings_files=['settings.toml', '.secrets.toml'])

    @app.route('/')
    def index():
        return 'Hello, World!' + app.config['REDIS_HOST']

    return app
