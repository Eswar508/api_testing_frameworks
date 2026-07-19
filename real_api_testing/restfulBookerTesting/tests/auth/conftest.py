import pytest
from utils.routes import Routes
@pytest.fixture(scope='session')
def auth_client(Base_session):
    Base_session.end_point(Routes.login)
    return Base_session