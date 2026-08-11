from testing_framework.clients.product_client import *
from testing_framework.clients.auth_client import login_client
import testing_framework.test_cases.login as login_test_cases
import testing_framework.test_cases.products as product_test_cases
def test_admin_workflow(product_to_post):
    # Admin can create a product
    login_payload=login_test_cases.admin
    login_response=login_client(login_payload)
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    admin_token = login_response.json()["access_token"]
    pr = post_product(product_to_post, token=admin_token)
    assert pr.status_code == 201
    assert pr.json()["name"]==product_to_post["name"]
    assert "product_id" in pr.json()
    # Admin can update the product
    id=pr.json()["product_id"]
    update_payload=product_test_cases.update_payload
    ur = update_product(id, update_payload, token=admin_token)
    assert ur.status_code == 200
    assert ur.json()["name"] == update_payload["name"]
    patch_payload=product_test_cases.patch_payload
    # Admin can partially update the product
    ptr = patch_product(id, patch_payload, token=admin_token)
    assert ptr.status_code == 200
    assert ptr.json()["name"] == patch_payload["name"]
    # Admin can delete the product
    response = delete_product(id, token=admin_token)
    assert response.status_code == 204