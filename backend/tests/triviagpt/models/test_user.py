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

        user11 = User.create_user(username='test_user11', reference='test_reference11')
        user_in_db = db.session.execute(select(User).where(User.username == 'test_user11')).first()

        assert user_in_db[0].username == 'test_user11'
        assert user_in_db[0].reference == 'test_reference11'