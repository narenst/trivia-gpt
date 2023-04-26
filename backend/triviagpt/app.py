from flask import Flask
from dynaconf import FlaskDynaconf

from triviagpt.db import init as init_db
from triviagpt.controllers import blue_print


def load_app_config(app, testing=False):
    """
    Load the configuration into Flask app using Dynaconf.
    """
    config = {}
    if testing:
        config = {
            'FORCE_ENV_FOR_DYNACONF': 'testing',
        }

    FlaskDynaconf(app, settings_files=['settings.toml', '.secrets.toml'], **config)
    return app


def create_app(testing=False):
    """
    Create and configure an instance of the Flask application.
    To run locally:
        flask --app triviagpt.app --debug run
    """
    # Create the Flask app
    app = Flask(__name__)
    
    # Load flask configuration into app config
    load_app_config(app, testing=testing)

    # Initialize db engine
    init_db(app)
    
    # Register routes via blueprints.
    app.register_blueprint(blue_print)

    return app