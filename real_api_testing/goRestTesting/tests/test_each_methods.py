import pytest
from utils.data import data as  load_data
from utils.log import log
r=log().info
Id=[None]
@pytest.mark.parametrize("P",load_data("TestCases/valid.json"))
def test_post_response(fed_session,P):
    global Id
    id,validate=fed_session.method_result("POST",201,"valid_json",data=P)
    assert validate["status_code"]
    assert validate["json_formate"]
    if id:
        Id.append(id)
    else:
        Id.append(None)
    print(f"posted id's: {Id}")
@pytest.mark.parametrize("i",range(1,len(load_data("TestCases/valid.json"))+1))
def test_get_response(fed_session,i):
    global Id
    if Id[i]==None:
        pytest.skip("got no id from post response")
    id,validate=fed_session.method_result("GET",200,"valid_json",id=Id[i])
    assert validate["status_code"]
    assert validate["json_formate"]
    if validate["json_formate"]:
        Id[0]=i
    print(f"got id's: {Id}")
def test_patch_response(fed_session):
    global Id
    try:
        #used Id[0] as an index of an id which has correct json formate else None
        i=Id[0]
        var=Id[i]
    except:
        pytest.exit("all get responses failed cannot proceed to further methods")
    r=fed_session.patch(var,{"name":"tirupati"})
    try:
        name=r.json()["name"]
        print(r.json())
    except:
        pytest.skip("json body of response of patch method is wrong/failed")
    assert name=="tirupati"
    print(f"patched id: {Id}")
def test_put_response(fed_session):
    global Id
    payload={"name":"hero","email":"hero@gmail.com","gender":"male","status":"active"}
    i=Id[0]
    r=fed_session.put(Id[i],payload)
    try:
        response=r.json()
        id=response["id"]
        B={"id":id,**payload}==response
        print(B)
        assert B
    except:
        pytest.skip("wrong json response")
    print(f"put id: {Id}")    
@pytest.mark.parametrize("i",range(1,len(load_data("TestCases/valid.json"))+1))
def test_delete_response(fed_session,i):
    global Id
    result=fed_session.method_result("DELETE",204,id=Id[i],return_only_bool=True)
    assert result
    print(f"existed id's: {Id}")