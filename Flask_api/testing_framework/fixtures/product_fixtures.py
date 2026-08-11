import pytest
from flask_api.data_base.data_services.product_services import *
from flask_api.data_base.data_clients.session import SessionLocal
from flask_api.data_base.data_clients.data_factory import product_factory
@pytest.fixture(scope="function")
def posted_product(session):
    product_data = {
        "name": "Test Product",
        "description": "This is a test product.",
        "price": 9.99,
        "stock": 10,
        "category_id": 1,
        "status": True
    }
    product = insert_product(product_data, session)
    yield product
    delete_product(product["product_id"], session)
@pytest.fixture(scope="function")
def product_to_post(session):
    product_data = {
        "name": "Test Post",
        "description": "This is a test product.",
        "price": 9.99,
        "stock": 10,
        "category_id": 1,
        "status": True
    }
    yield product_data
    products=get_products({"name": product_data["name"]}, session=session)
    if products:
        delete_product(products[0]["product_id"], session)
@pytest.fixture(scope="function")
def deleted_product_id(session, posted_product):
    delete_product(posted_product["product_id"], session)
    return posted_product["product_id"]