import responses
import requests
import pytest
from mock_api.CRUD_client.supply_data import Test_cases
from jsonschema import validate
@responses.activate
@pytest.mark.parametrize("id",Test_cases.get())
def test_get_valid_ids(mocked_get,id,schema):
    r=requests.post(f"http://calc.com/{id}")
    assert r.status_code ==200
    try:
        validate(r.json(),schema)
        assert True
    except:assert False
    print(r.json())