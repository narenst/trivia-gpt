from triviagpt.db import db
from triviagpt.models.user import User

from tests.triviagpt.conftest import app

from sqlalchemy import select


def test_create_user(app):
    """
    Test creating a user.
    And verifying that the user is in the database.
    """

    with app.app_context():
        
        print(app.config.current_env)
        print(app.config.TESTING)

        user11 = User.create_user(username='test_user_create', reference='test_reference_create')
        user_in_db = db.session.execute(select(User).where(User.username == 'test_user_create')).first()[0]

        assert user_in_db.username == 'test_user_create'
        assert user_in_db.reference == 'test_reference_create'
        

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
