import pytest
import requests
from wiremock.testing.testcontainer import wiremock_container
from wiremock.constants import Config, HttpMethods
from wiremock.resources.mappings import Mappings,Mapping,MappingRequest,MappingResponse
@pytest.fixture(scope="session")
def wiremock_server():
    with wiremock_container(secure=False) as wm:
        Config.base_url=wm.get_url("__admin")
    Mappings.create_mapping(
        Mapping(
            request=MappingRequest(method=HttpMethods.GET,url="/v1/inventory"),
            response=MappingResponse(status=200,body='{"status":"in_stock","count:24}'),
            persistent=False
        )
    )
    yield wm
def test_inventory_service_against_container(wiremock_server):
    target_url=wiremock_server.get_url("/v1/inventory")
    response=requests.get(target_url)
    assert response.status_code ==200
    assert response.json()["count"]==24