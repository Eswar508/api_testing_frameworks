import pytest
import responses,requests
from mock_api.CRUD_client.supply_data import Test_cases
@responses.activate
@pytest.mark.parametrize(("id","data"),Test_cases.patch().items())
def test_patch(id,data,mocked_partial_update):
    get_r=requests.get(f"http://calc.com/{id}")
    print(get_r.json())
    expected_data={**get_r.json(),**data}
    r=requests.patch(f"http://calc.com/{id}",json=data)
    assert r.status_code == 200
    assert r.json() == expected_data
