import pytest
import responses
import requests
from mock_api.CRUD_client.supply_data import Test_cases
@responses.activate
@pytest.mark.parametrize("data",Test_cases.post())
def test_s(data,mocked_post):
    s=requests.session()
    r=s.post("http://calc.com",json=data)
    assert r.status_code == 201
    assert r.json() ==data