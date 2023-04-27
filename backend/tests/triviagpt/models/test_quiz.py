from tests.triviagpt.conftest import app
from triviagpt.db import db
from triviagpt.models.user import User
from triviagpt.models.quiz import Quiz

from sqlalchemy import select
from datetime import datetime, timedelta


def test_create_quiz(app, test_user):
    """
    Test creating a quiz.
    And verifying that the quiz is in the database.
    """
    with app.app_context():

        quiz11 = Quiz.create_quiz(user=test_user, total_questions=10)
        quiz_in_db = db.session.execute(select(Quiz).where(Quiz.user_id == test_user.id)).first()[0]

        assert quiz_in_db.user_id == test_user.id
        assert quiz_in_db.total_questions == 10
        assert quiz_in_db.current_question == 1
        assert (datetime.utcnow() - quiz_in_db.dt_created) < timedelta(minutes=10)
        assert quiz_in_db.user == test_user


def test_delete_user_with_quiz(app, test_user, test_quiz):
    """
    Test deleting a user with a quiz.
    Quizzes should be deleted with the user.
    """
    with app.app_context():
        User.delete_user(user=test_user)
        assert db.session.execute(select(User).where(User.id == test_user.id)).first() is None
        assert db.session.execute(select(Quiz).where(Quiz.id == test_quiz.id)).first() is None