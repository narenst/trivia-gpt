from triviagpt.controllers import blue_print
from triviagpt.models.quiz import Quiz
from triviagpt.models.user import User
from triviagpt.services.openai import OpenAIService

from flask import jsonify


@blue_print.route('/quiz/create/<username>', methods=['POST', 'GET'])
def create_quiz(username: str):
    """
    Create a quiz for a user.
    """
    user = User.get_user_by_username(username=username)
    if not user:
        return "User not found.", 404
    
    quiz = Quiz.create_quiz(user=user, total_questions=10)
    return jsonify(quiz.to_dict())


@blue_print.route('/quiz/<quiz_id>/next_question')
def get_next_question(quiz_id: int):
    """
    Get the next question for a quiz.
    """
    quiz = Quiz.get_quiz_by_id(quiz_id=quiz_id)
    if not quiz:
        return "Quiz not found.", 404
    
    if quiz.current_question > quiz.total_questions:
        return "Quiz is complete.", 200

    # Call ChatGPT to get the next question.
    difficulty = quiz.current_question
    question_text = OpenAIService.get_quiz_question(difficulty=difficulty)

    # Bump up the current question number.
    quiz.increment_current_question()

    # Include the question text in the response.
    response = quiz.to_dict()
    response.update({"question_text": question_text,
                     "difficulty": difficulty})

    return jsonify(response)