from testing_framework.clients.product_client import get_products
import testing_framework.test_cases.token as t
def test_valid_token(admin_token):
    response=get_products(token=admin_token)
    assert response.status_code == 200
def test_missing_token():
    response=get_products(token="")
    assert response.status_code == 401
def test_expired_token():
    expired_token=t.expired_token
    response=get_products(token=expired_token)
    assert response.status_code == 401
def test_invalid_signature_token(admin_token):
    invalid_signature=t.genereate_invalid_signature_token(admin_token)
    response=get_products(token=invalid_signature)
    assert response.status_code == 401
def test_tampered_token(admin_token):
    tampered_token=t.generate_tampered_token(admin_token)
    response=get_products(token=tampered_token)
    assert response.status_code == 401
def test_malformed_token():
    malformed_token=t.malformed_token
    response=get_products(token=malformed_token)
    assert response.status_code == 401
def test_wrong_algorithm_token():
    wrong_algorithm_token=t.generate_wrong_algorithm_token()
    response=get_products(token=wrong_algorithm_token)
    assert response.status_code == 401