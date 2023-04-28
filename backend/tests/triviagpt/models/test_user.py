from tests.triviagpt.conftest import app, test_user, test_quiz
from triviagpt.db import db
from triviagpt.models.user import User

from sqlalchemy import select
from datetime import datetime, timedelta


def test_create_user(app):
    """
    Test creating a user.
    And verifying that the user is in the database.
    """

    with app.app_context():

        user11 = User.create_user(username='test_user_create', reference='test_reference_create')
        user_in_db = db.session.execute(select(User).where(User.username == 'test_user_create')).first()[0]

        assert user_in_db.username == 'test_user_create'
        assert user_in_db.reference == 'test_reference_create'
        assert (datetime.utcnow() - user_in_db.dt_created) < timedelta(minutes=10)
        

def test_get_user_by_username(app, test_user):
    """
    Test getting a user by username.
    """
    with app.app_context():
        user = User.get_user_by_username(username='test_user')
        assert user.username == 'test_user'
        assert user.reference == 'test_reference'


def test_get_user_by_reference(app, test_user):
    """
    Test getting a user by reference.
    """
    with app.app_context():
        user = User.get_user_by_reference(reference='test_reference')
        assert user.username == 'test_user'
        assert user.reference == 'test_reference'


def test_get_quizzes_for_user(app, test_quiz):
    """
    Test if user.quizzes is populated
    """
    with app.app_context():
        user = User.get_user_by_id(user_id=test_quiz.user_id)

        assert len(user.quizzes) == 1
        assert user.quizzes[0].id == test_quiz.id


def test_get_non_existent_user(app):
    """
    Test getting a non-existent user.
    """
    with app.app_context():
        user = User.get_user_by_username(username='non_existent_user')
        assert user is None

        user = User.get_user_by_id(user_id=999)
        assert user is None

        user = User.get_user_by_reference(reference='non_existent_reference')
        assert user is None