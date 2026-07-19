import requests,os,time
import pytest
from utils.data import data
from utils.feed_session import FedSession
@pytest.fixture(scope="session")
def response():
    API="https://gorest.co.in/public/v2"
    token='6c5909f00d0b785d5cdc4514ee20960d7c67a8951c1001ccf1b6421e0f1a8b1a'
    s=requests.session()
    s.headers.update({
        "Authorization":f"Bearer {token}",
        "Accept":"application/json",
        "Content-Type":"application/json",
    })
    schema=data("schemas\list.json")
    yield (s,API,schema)
@pytest.fixture(scope="session")
def fed_session(response):
    yield FedSession(*response)
#@pytest.fixture(scope="session")
#def tm():
#    yield Testmethod()