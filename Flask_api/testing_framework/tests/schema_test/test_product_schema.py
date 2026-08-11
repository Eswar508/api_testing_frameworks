from testing_framework.clients.product_client import *
from testing_framework.utils.validate_schema import validate_product_schema
import testing_framework.test_cases.products as test_cases
def test_get_product_schema(posted_product,admin_token):
    response = get_product(posted_product["product_id"], token=admin_token)
    assert response.status_code == 200
    assert validate_product_schema(response.json())
def test_post_product_schema(product_to_post,admin_token):
    response=post_product(product_to_post,admin_token)
    assert response.status_code == 201
    assert validate_product_schema(response.json())
def test_patch_product_schema(posted_product,admin_token):
    payload=test_cases.patch_payload
    response=patch_product(posted_product["product_id"],payload,admin_token)
    assert response.status_code == 200
    assert validate_product_schema(response.json())
def test_update_product_schema(posted_product,admin_token):
    payload=test_cases.update_payload
    response=patch_product(posted_product["product_id"],payload,admin_token)
    assert response.status_code == 200
    assert validate_product_schema(response.json())