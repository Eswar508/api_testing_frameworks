import pytest
from utils.routes import Routes
@pytest.fixture(scope="session")
def booking_client(Base_session):
    Base_session.end_point(Routes.booking)
    return Base_session