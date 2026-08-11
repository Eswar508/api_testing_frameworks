from testing_framework.clients.product_client import get_products,get_product
def test_get_products(admin_token):
    response = get_products(token=admin_token)
    assert response.status_code == 200
def test_get_product_with_with_valid_id(admin_token, posted_product):
    response = get_product(posted_product["product_id"], token=admin_token)
    assert response.status_code == 200
def test_get_product_with_invalid_id(admin_token):
    invalid_id = "invalid_id"
    response = get_product(invalid_id, token=admin_token)
    assert response.status_code == 404
def test_get_deleted_id(admin_token,deleted_product_id):
    response = get_product(deleted_product_id, token=admin_token)
    assert response.status_code == 404