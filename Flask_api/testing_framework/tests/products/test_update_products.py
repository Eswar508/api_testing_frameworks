from testing_framework.clients.product_client import update_product
import testing_framework.test_cases.products as test_cases
def test_update_product(admin_token, posted_product):
    update_payload = test_cases.update_payload
    response = update_product(posted_product["product_id"], update_payload, token=admin_token)
    assert response.status_code == 200
def test_update_with_invalid_fields(admin_token, posted_product):
    invalid_update_payload = test_cases.invalid_update_payload
    response = update_product(posted_product["product_id"], invalid_update_payload, token=admin_token)
    assert response.status_code == 422
def test_update_product_with_duplicate_fields(admin_token, posted_product):
    payload=test_cases.duplicate_update_payload
    response = update_product(posted_product["product_id"], payload, token=admin_token)