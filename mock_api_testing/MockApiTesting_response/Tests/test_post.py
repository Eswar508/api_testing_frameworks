import pytest
import responses
import requests
from mock_api.CRUD_client.supply_data import Test_cases
@responses.activate
@pytest.mark.parametrize("data",Test_cases.post())
def test_post_valid_data(data,mocked_post):
    r=requests.post("http://calc.com",json=data)
    assert r.json()== data
    assert r.status_code ==201