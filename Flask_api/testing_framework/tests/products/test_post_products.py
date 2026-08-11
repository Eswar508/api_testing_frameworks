from testing_framework.clients.product_client import post_product
import testing_framework.test_cases.products as test_cases

def test_post_valid_product(admin_token, product_to_post):
    response = post_product(product_to_post, token=admin_token)
    assert response.status_code == 201
def test_post_product_with_missing_fields(admin_token):
    missing_fields_payload = test_cases.missing_fields_payload
    response = post_product(missing_fields_payload, token=admin_token)
    assert response.status_code == 422
def test_post_product_with_invalid_fields(admin_token):
    invalid_fields_payload = test_cases.invalid_fields
    response = post_product(invalid_fields_payload, token=admin_token)
    assert response.status_code == 422
def test_post_product_with_duplicate_fields(admin_token):
    duplicate_fields_payload = test_cases.duplicate_fields
    response = post_product(duplicate_fields_payload, token=admin_token)
    assert response.status_code == 403