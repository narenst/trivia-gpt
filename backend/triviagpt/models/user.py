from triviagpt.db import db
from triviagpt.models.base import BaseModel

from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column, Session

from typing import Optional


class User(db.Model):
    """
    Defines the User model.
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    reference: Mapped[str] = mapped_column(String(30))
    param: Mapped[Optional[str]] = mapped_column(String(30))


    @staticmethod
    def create_user(username: str, reference: str):
        """
        Create a user.
        """
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
        return db.session.execute(select(User).where(User.username == username)).first()
        


    @staticmethod
    def get_user_by_reference(reference: str):
        """
        Get a user by reference.
        """        
        return db.session.execute(select(User).where(User.reference == reference)).first()


    def __repr__(self) -> str:
        """
        String representation of the User model.
        """
        return f"User(id={self.id}, username={self.username}, reference={self.reference})"