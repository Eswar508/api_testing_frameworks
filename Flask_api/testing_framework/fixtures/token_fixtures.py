import pytest
from flask_api.helper_fun import generate_token

@pytest.fixture(scope="session")
def admin_token():
    return generate_token(id=1, role="admin")
@pytest.fixture(scope="session")
def staff_token():
    return generate_token(id=3, role="staff")