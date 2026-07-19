import pytest
from utils.data import data
import time
@pytest.mark.parametrize("data",data("TestCases/created.json"))
def test_sucessfully_created(fed_session,data):
    assert fed_session.method_result("POST",201,"valid_json",data,return_only_bool=True)
    time.sleep(1)
@pytest.mark.parametrize("data",data("TestCases/invalid.json"))
def test_unprocessable_data(fed_session,data):
    assert fed_session.method_result("POST",422,"invalid_fields",data=data,return_only_bool=True)
    time.sleep(1)