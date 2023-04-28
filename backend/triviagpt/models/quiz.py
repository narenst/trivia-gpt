from triviagpt.db import db, utcnow

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime, select

from datetime import datetime


class Quiz(db.Model):
    """
    Defines the Quiz model.
    Each quiz is attached to a user.
    It tracks the total number of questions, current question number and current score
    """
    __tablename__ = 'quizzes'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))

    total_questions: Mapped[int] = mapped_column(Integer, default=10)
    current_question: Mapped[int] = mapped_column(Integer, default=1)
    dt_created: Mapped[datetime] = mapped_column(DateTime, server_default=utcnow())

    user: Mapped["User"] = relationship("User", back_populates="quizzes")


    @staticmethod
    def create_quiz(user: "User", total_questions: int = 10):
        """
        Create a new quiz.
        """
        quiz = Quiz(user=user, total_questions=total_questions)
        db.session.add(quiz)
        db.session.commit()
        db.session.refresh(quiz)
        return quiz

    @staticmethod
    def get_quiz_by_id(quiz_id: int):
        """
        Get a quiz by id.
        """
        rows = db.session.execute(select(Quiz).where(Quiz.id == quiz_id)).first()
        if rows:
            return rows[0]
        else:
            return None
        
    def increment_current_question(self):
        """
        Increment the current question number.
        """
        self.current_question += 1
        db.session.add(self)
        db.session.commit()
        return self
    
    def to_dict(self):
        """
        Return a dictionary representation of the quiz.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_questions": self.total_questions,
            "current_question": self.current_question,
            "dt_created": self.dt_created
        }