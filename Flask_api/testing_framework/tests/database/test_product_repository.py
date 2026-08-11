from flask_api.data_base.data_services.product_services import *
from flask_api.data_base.tables.products import Product    
import testing_framework.test_cases.products as t
def test_get_repository(posted_product,session):
    # Test implementation for get_repository
    p=get_product(posted_product['product_id'], session)
    assert p is not None
    assert p["name"] == posted_product["name"]
def test_insert_product(product_to_post,session):
    # Test implementation for insert_product
    product = insert_product(product_to_post, session)
    assert product is not None
    assert product["name"] == product_to_post["name"]
def test_update_product(posted_product,session):
    # Test implementation for update_product
    updated_data = t.update_payload
    updated_product = update_product(posted_product['product_id'], updated_data, session)
    assert updated_product is not None
    assert updated_product["name"] == updated_data["name"]
def test_patch_product(posted_product,session):
    # Test implementation for patch_product
    patch_data = t.patch_payload
    patched_product = update_product(posted_product['product_id'], patch_data, session)
    assert patched_product is not None
    assert patched_product["name"] == patch_data["name"]
def test_delete_product(posted_product,session):
    # Test implementation for delete_product
    delete_product(posted_product['product_id'], session)
    deleted_product = get_product(posted_product['product_id'], session)
    assert deleted_product is None