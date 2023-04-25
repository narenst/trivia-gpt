from triviagpt.app import create_app
from triviagpt.db import init as init_db, db

import pytest
from sqlalchemy import text

@pytest.fixture()
def app():
    """
    Create and configure a new app instance for each test.
    Ensure the testing database is already created.
    """
    app = create_app(testing=True)

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()