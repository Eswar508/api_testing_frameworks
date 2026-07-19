import pytest
import responses,requests
from mock_api.CRUD_client.supply_data import Test_cases
@responses.activate
@pytest.mark.parametrize(("id","data"),Test_cases.put().items())
def test_put(id,data,mocked_update):
    r=requests.put(f"http://calc.com/{id}",json=data)
    assert r.status_code == 200
    assert r.json() == data