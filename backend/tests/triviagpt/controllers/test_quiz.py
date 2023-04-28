from triviagpt.models.quiz import Quiz
from triviagpt.services.openai import OpenAIService
from triviagpt.db import db
from tests.triviagpt.conftest import client, test_user, test_quiz

from unittest.mock import patch


def test_create_quiz(client, test_user):
    """
    Test creating a new quiz for a user
    """
    response = client.get(f'/quiz/create/{test_user.username}')

    assert response.status_code == 200
    assert response.json['id'] is not None
    assert response.json['user_id'] == test_user.id
    assert response.json['total_questions'] == 10
    assert response.json['current_question'] == 1


def test_create_quiz_for_nonexistent_user(client):
    """
    Test creating a new quiz for a user that doesn't exist.
    """
    response = client.get(f'/quiz/create/doesntexist')

    assert response.status_code == 404
    assert response.text == 'User not found.'


def test_get_next_question(client, test_quiz):
    """
    Test getting the next question for a quiz.
    Mock the openai call.
    """

    open_ai_response = {
        "question": "What is the capital of the United States?",
        "choices": ["New York", "Washington, D.C.", "Los Angeles"],
        "answer": "Washington, D.C."
    }

    with patch.object(OpenAIService, 'get_quiz_question', return_value=open_ai_response) as openai_mock:
        response = client.get(f'/quiz/{test_quiz.id}/next_question')

        assert response.status_code == 200
        assert response.json['id'] == test_quiz.id
        assert response.json['user_id'] == test_quiz.user_id
        assert response.json['total_questions'] == 10
        assert response.json['question_text'] == open_ai_response
        assert response.json['difficulty'] == 1
        assert response.json['current_question'] == 2

        openai_mock.assert_called_once_with(difficulty=1)

    
def test_get_next_question_quiz_complete(app, client, test_quiz):
    """
    Test getting the next question for a quiz.
    Mock the openai call.
    """

    with app.app_context():
        quiz = Quiz.query.get(test_quiz.id)
        quiz.current_question = 11
        db.session.commit()

    with patch.object(OpenAIService, 'get_quiz_question', return_value=None) as openai_mock:
        response = client.get(f'/quiz/{test_quiz.id}/next_question')

        assert response.status_code == 200
        assert response.text == 'Quiz is complete.'

        openai_mock.assert_not_called()


def test_get_next_question_quiz_not_found(client):
    """
    Test getting the next question for a quiz that does not exist
    """
    
    response = client.get(f'/quiz/999/next_question')

    assert response.status_code == 404
    assert response.text == 'Quiz not found.'