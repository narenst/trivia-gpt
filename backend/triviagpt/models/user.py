from triviagpt.db import db, utcnow
from triviagpt.models.base import BaseModel

from sqlalchemy import DateTime, String, select
from sqlalchemy.orm import Mapped, mapped_column

import random
import string
from datetime import datetime
from typing import List


class User(db.Model):
    """
    Defines the User model.
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    reference: Mapped[str] = mapped_column(String(30))
    dt_created: Mapped[datetime] = mapped_column(DateTime, server_default=utcnow())
    
    quizzes: Mapped[List["Quiz"]] = db.relationship("Quiz", back_populates="user", cascade="all, delete-orphan")


    @staticmethod
    def create_user(reference: str, username: str = None):
        """
        Create a user.
        """
        if not username:
            username = generate_random_username()

        user = User(username=username, reference=reference)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return user


    @staticmethod
    def get_user_by_username(username: str):
        """
        Get a user by username.
        """
        return db.session.query(User).filter(User.username == username).first()


    @staticmethod
    def get_user_by_reference(reference: str):
        """
        Get a user by reference.
        """
        return db.session.query(User).filter(User.reference == reference).first()


    @staticmethod
    def get_user_by_id(user_id: int):
        """
        Get a user by id.
        """
        return db.session.query(User).get(user_id)


    @staticmethod
    def delete_user(user: "User"):
        """
        Delete a user.
        """
        db.session.delete(user)
        db.session.commit()


    def __repr__(self) -> str:
        """
        String representation of the User model.
        """
        return f"User(id={self.id}, username={self.username}, reference={self.reference})"
    

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the User model.
        """
        return {
            'id': self.id,
            'username': self.username,
            'reference': self.reference,
            'quizzes': [quiz.to_dict() for quiz in self.quizzes if self.quizzes] if self.quizzes else []
        }


def generate_random_username():
    """
    Generate a random string of length 15.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=15))