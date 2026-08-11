from testing_framework.clients.product_client import delete_product
def test_delete_product(admin_token, posted_product):
    response = delete_product(posted_product["product_id"], token=admin_token)
    assert response.status_code == 204
def test_delete_deleted_id(admin_token, deleted_product_id):
    # First, delete the product
    delete_response = delete_product(deleted_product_id, token=admin_token)
    assert delete_response.status_code == 404
def test_delete_non_existing_id(admin_token):
    non_existing_id = 9999  # Assuming this ID does not exist
    response = delete_product(non_existing_id, token=admin_token)
    assert response.status_code == 404