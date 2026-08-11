from testing_framework.clients.product_client import patch_product
import testing_framework.test_cases.products as test_cases
def test_patch_product(admin_token, posted_product):
    patch_payload = test_cases.patch_payload
    response = patch_product(posted_product["product_id"], patch_payload, token=admin_token)
    assert response.status_code == 200
def test_patch_with_invalid_fields(admin_token, posted_product):
    invalid_patch_payload = test_cases.invalid_patch_payload
    response = patch_product(posted_product["product_id"], invalid_patch_payload, token=admin_token)
    assert response.status_code == 422
def test_patch_product_with_duplicate_fields(admin_token, posted_product):
    duplicate_patch_payload = test_cases.duplicate_patch_payload
    response = patch_product(posted_product["product_id"], duplicate_patch_payload, token=admin_token)
    assert response.status_code == 403