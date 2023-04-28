from triviagpt.app import create_app
from triviagpt.db import init as init_db, db
from triviagpt.models.user import User
from triviagpt.models.quiz import Quiz

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


@pytest.fixture()
def client(app):
    """
    A test client for the app.
    """
    return app.test_client()


@pytest.fixture()
def test_user(app):
    """
    Create a test user.
    """
    with app.app_context():
        user = User.create_user(username='test_user', reference='test_reference')

    yield user


@pytest.fixture()
def test_quiz(app, test_user):
    """
    Create a test quiz.
    """
    with app.app_context():
        quiz = Quiz.create_quiz(user=test_user, total_questions=10)

    yield quiz