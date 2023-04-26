from triviagpt.db import db
from triviagpt.models.base import BaseModel

from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column

import random
import string


class User(db.Model):
    """
    Defines the User model.
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    reference: Mapped[str] = mapped_column(String(30))
    


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
        rows = db.session.execute(select(User).where(User.username == username)).first()
        if rows:
            return rows[0]
        else:
            return None


    @staticmethod
    def get_user_by_reference(reference: str):
        """
        Get a user by reference.
        """
        rows = db.session.execute(select(User).where(User.reference == reference)).first()
        if rows:
            return rows[0]
        else:
            return None


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
            'username': self.username,
            'reference': self.reference
        }


def generate_random_username():
    """
    Generate a random string of length 15.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=15))