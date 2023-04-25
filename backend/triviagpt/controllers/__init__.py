from flask import Blueprint

blue_print = Blueprint('main', __name__)

# Importing the controllers here will register the routes.
from triviagpt.controllers import user