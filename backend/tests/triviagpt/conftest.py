from triviagpt.app import create_app
from triviagpt.db import init as init_db, db
from triviagpt.models.user import User

import pytest
from sqlalchemy import text

@pytest.fixture(scope='session')
def app():
    """
    Create and configure a new app instance for each test.
    Ensure the testing database is already created.
    """
    app = create_app(testing=True)

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    """
    A test client for the app.
    """
    return app.test_client()


@pytest.fixture
def test_user(app):
    """
    Create a test user.
    """
    with app.app_context():
        user = User.create_user(username='test_user', reference='test_reference')
        yield user

        db.session.execute(text("DELETE FROM users WHERE id=:id"), {'id': user.id})
        db.session.commit()
        db.session.close()