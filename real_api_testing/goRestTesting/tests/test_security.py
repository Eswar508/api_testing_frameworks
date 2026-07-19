import pytest
from utils.data import data
import time
from jsonschema import validate
from utils.log import log
logger=log()
count=1
@pytest.mark.parametrize("data",data("TestCases/sample.json"))
def test_authentication_validation(response,data):
    global count
    s,api,schema=response
    if count == 1:
        token='6c5909f00d0b785d5cdc4514ee20960d7c67a8951c1001ccf1b6421e0f1a8b1b'
        s.headers.update({"Authorization":f"Bearer {token}"})
        count+=1
    elif count == 2:
        del s.headers["Authorization"]
    r=s.post(f"{api}/users",json=data)
    b=False
    try:
        validate(r.json(),schema["invalid_json"])
        b=True
    except:
        pass
    if b and r.status_code == 401:
        assert True
    else:
        assert False
    logger.info(r.json())
    logger.info(r.status_code)
    time.sleep(1)
@pytest.mark.parametrize("method",["patch","delete"])
def test_accessing_other_fields(method,response):
    s,api,schema=response
    if method=="patch":
        r=s.request(method,f"{api}/users/{8474362}",json={"name":"Gandi"})
        logger.info(r.json())
        logger.info(r.status_code)
        if r.status_code == 200:
            assert False
        else:
            assert True
    elif method == "delete":
        r=s.request(method,f"{api}/users/{8474362}")
        logger.info(r.status_code)
        if r.status_code == 204:
            assert False
        else:
            assert True