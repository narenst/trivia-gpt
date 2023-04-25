import unittest
import pytest

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


from triviagpt.models.user import User

class TestUser():

    @pytest.fixture(autouse=True)
    def init_db(self):
        engine = create_engine('sqlite:///:memory:')
        BaseModel.metadata.create_all(engine)
        self.session = Session(engine)

    @classmethod
    def setUpClass(cls) -> None:
        engine = create_engine('sqlite:///:memory:')
        cls.session = Session(engine)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

    @mock.patch('triviagpt.models.user.get_sql_alchemy_engine', return_value=self.session)
    def test_create_user(self):
        user1 = User.create_user(username='test_user', reference='test_reference')

        user_in_db = self.session.execute(select(User).where(User.username == 'test_user')).first()
        self.assertEqual(user_in_db.username, 'test_user')
        self.assertEqual(user_in_db.password, 'password')