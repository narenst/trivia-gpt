from app import create_app

import pytest

@pytest.fixture
def initialize_app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    return app