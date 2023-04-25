from triviagpt.controllers import blue_print
from triviagpt.db import get_sql_alchemy_engine
from triviagpt.models.base import BaseModel
from triviagpt.models.user import User


@blue_print.route('/')
def index():
    user = User.get_user_by_username(username='testusername')
    return 'Hello, World! ' + str(user)

@blue_print.route('/load')
def load():
    BaseModel.metadata.create_all(get_sql_alchemy_engine())
    return 'Loaded!'

@blue_print.route('/create')
def create():
    new_user = User.create_user(username='testusername', reference='test')
    return 'Created! + ' + str(new_user)