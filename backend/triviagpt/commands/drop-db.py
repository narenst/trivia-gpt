from triviagpt.app import create_app
from triviagpt.db import db
from triviagpt.models.user import User
from triviagpt.models.quiz import Quiz

import click


app = create_app()

@click.command("drop-db")
def drop_db():
    """
    Delete the database tables.
    """
    with app.app_context():
        db.drop_all()
        print("Database tables dropped.")

if __name__ == "__main__":
    drop_db()