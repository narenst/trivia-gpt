from triviagpt.app import create_app
from triviagpt.db import db
from triviagpt.models.user import User
from triviagpt.models.quiz import Quiz

import click


app = create_app()

@click.command("setup-db")
def setup_db():
    """
    Create the database tables.
    """
    with app.app_context():
        db.create_all()
        print("Database tables created.")

if __name__ == "__main__":
    setup_db()