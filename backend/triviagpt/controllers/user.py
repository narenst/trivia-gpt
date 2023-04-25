from triviagpt.controllers import blue_print
from triviagpt.db import db, get_sql_alchemy_engine
from triviagpt.models.base import BaseModel
from triviagpt.models.user import User

from sqlalchemy import select


@blue_print.route('/')
def index():
    users = db.session.execute(select(User)).scalars()
    return 'All users! ' + str([u for u in users])

@blue_print.route('/load')
def load():
    BaseModel.metadata.create_all(get_sql_alchemy_engine())
    return 'Loaded!'

@blue_print.route('/get/<username>')
def get(username):
    user = User.get_user_by_username(username=username)
    return 'Got! ' + str(user)

@blue_print.route('/create/<username>')
def create(username):
    new_user = User.create_user(username=username, reference=f'{username}_ref')
    return 'Created! + ' + str(new_user)