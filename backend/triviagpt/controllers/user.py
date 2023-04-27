from triviagpt.controllers import blue_print
from triviagpt.models.user import User

from sqlalchemy import select
from flask import jsonify


@blue_print.route('/user/get_or_create_by_reference/<reference>')
def get_or_create_by_reference(reference: str):
    """
    Look up a user by reference.
    If the user does not exist, create it.
    Returns json of the user.
    """
    user = User.get_user_by_reference(reference=reference)
    if not user:
        user = User.create_user(reference=reference)
    return jsonify(user.to_dict())


@blue_print.route('/user/get_by_username/<username>')
def get_user_by_username(username: str):
    """
    Get a user by username.
    """        
    user = User.get_user_by_username(username=username)
    if not user:
        return "User not found.", 404
    return jsonify(user.to_dict())