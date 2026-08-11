import pytest
import testing_framework.test_cases.login as login_test_case
import testing_framework.test_cases.products as product_test_case
from testing_framework.clients.auth_client import login_client
from testing_framework.clients.product_client import get_products,get_product
def test_staff_workflow(posted_product):
    # Staff can view products
    login_payload = login_test_case.staff
    login_response = login_client(login_payload)
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    staff_token = login_response.json()["access_token"]
    get_response = get_products(token=staff_token)
    assert get_response.status_code == 200
    get_product_response = get_product(posted_product["product_id"], token=staff_token)
    assert get_product_response.status_code == 200