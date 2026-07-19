import pytest
import responses,requests
from mock_api.CRUD_client.supply_data import Test_cases
@responses.activate
@pytest.mark.parametrize("id",Test_cases.delete())
def test_delete(id,mocked_delete):
    r=requests.delete(f"http://calc.com/{id}")
    r.status_code=200
    expected={"message":f"deleted id {id}"}
    r.json() == expected