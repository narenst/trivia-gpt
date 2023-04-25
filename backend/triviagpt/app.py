from flask import Flask
from dynaconf import FlaskDynaconf

from triviagpt.db import init as init_db
from triviagpt.models.base import BaseModel
from triviagpt.models.user import User
from triviagpt.controllers import blue_print


def create_app():
    """
    Create and configure an instance of the Flask application.
    To run locally:
        flask --app triviagpt.app --debug run
    """
    # Create the Flask app
    app = Flask(__name__)
    
    # Load flask configuration into app config
    FlaskDynaconf(app, settings_files=['settings.toml', '.secrets.toml'])

    # Initialize db engine
    init_db(app)
    
    # Register routes via blueprints.
    app.register_blueprint(blue_print)

    return app
