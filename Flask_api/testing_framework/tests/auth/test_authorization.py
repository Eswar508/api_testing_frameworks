from testing_framework.clients.product_client import *
import testing_framework.test_cases.products as t
def test_admin_can_create_product(admin_token,product_to_post):
    response=post_product(product_to_post,token=admin_token)
    assert response.status_code==201
def test_admin_can_update_product(admin_token,posted_product):
    payload=t.update_payload
    response=update_product(posted_product["product_id"], payload, token=admin_token)
    assert response.status_code==200
def test_admin_can_partial_update_product(admin_token,posted_product):
    payload=t.patch_payload
    response=patch_product(posted_product["product_id"], payload, token=admin_token)
    assert response.status_code==200
def test_admin_can_delete_product(admin_token,posted_product):
    response=delete_product(posted_product["product_id"], token=admin_token)
    assert response.status_code==204

def test_staff_can_view_stock(staff_token,posted_product):
    response=get_product(posted_product["product_id"],token=staff_token)
    assert response.status_code==200

def test_staff_cannot_create_product(staff_token,product_to_post):
    response=post_product(product_to_post,token=staff_token)
    assert response.status_code==403

def test_staff_cannot_update_product(staff_token,posted_product):
    payload=t.update_payload
    response=update_product(posted_product["product_id"], payload, token=staff_token)
    assert response.status_code==403
def test_staff_cannot_partial_update_product(staff_token,posted_product):
    payload=t.patch_payload
    response=patch_product(posted_product["product_id"], payload, token=staff_token)
    assert response.status_code==403
def test_staff_cannot_delete_product(staff_token,posted_product):
    response=delete_product(posted_product["product_id"], token=staff_token)
    assert response.status_code==403