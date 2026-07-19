import pytest
import requests
# 1. Correct Import Paths
from wiremock.constants import Config
from wiremock.resources.mappings.models import HttpMethods
from wiremock.testing.testcontainer import wiremock_container

# Mappings, Mapping, MappingRequest, MappingResponse all live inside wiremock.client
from wiremock.client import Mappings, Mapping, MappingRequest, MappingResponse

@pytest.fixture(scope="session")
def wiremock_server():
    """Spins up an independent out-of-process WireMock Docker Container"""
    with wiremock_container(secure=False) as wm:
        # Config.base_url is verified to exist here
        Config.base_url = wm.get_url("__admin")
        
        # Define and register the mapping stub
        Mappings.create_mapping(
            Mapping(
                request=MappingRequest(method=HttpMethods.GET, url="/v1/inventory"),
                response=MappingResponse(status=200, body='{"status": "in_stock", "count": 24}'),
                persistent=False
            )
        )
        yield wm

def test_inventory_service_against_container(wiremock_server):
    # Hit the live out-of-process Docker container port
    target_url = wiremock_server.get_url("/v1/inventory")
    response = requests.get(target_url)
    
    assert response.status_code == 200
    assert response.json()["count"] == 24