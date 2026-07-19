from jsonschema import validate
import json
from mock_api.CRUD_client.supply_data import get_id
def post(request,Schema=None):
    data=json.loads(request.body)
    try:
        validate(data,Schema)
    except:return (422,{},json.dumps({"error":"invalid input"}))
    with open("mock_api/jsons/data_storage/post.json") as f:
        d=json.load(f)
    id=get_id()
    if data not in d.values():
        d.update({id:data})
        with open("mock_api/jsons/data_storage/post.json","w") as f0:
            json.dump(d,f0,indent=4)
        r=(201,{},json.dumps(data))
        return r
    return (404,{},json.dumps({"error":"data already exists"}))
def get(request,storage=None):
    id=request.url.split("/")[-1]
    if id in storage:
        d=storage[id]
        headers={"requested_id":str(id)}
        return (200,headers,json.dumps(d))
    return (
    404,
    {},
    json.dumps({"message": "User not found"})
    )
def partial_update(request,storage=None,schema=None):
    updates=json.loads(request.body)
    id=request.url.split("/")[-1]
    if id in storage:
        try:
            validate(updates,schema)
            storage[id]={**storage[id],**updates}
            print(storage)
            with open("mock_api/jsons/data_storage/partial_update.json","w") as pu:
                json.dump(storage,pu,indent=4)
            return (200,{},json.dumps(storage[id]))
        except:
            return (422,{},json.dumps({"error":"invalid field"}))
    return (404,{},json.dumps({"error":"id is not valid"}))
def update(request,storage=None,schema=None):
    updates=json.loads(request.body)
    id=request.url.split("/")[-1]
    if id in storage:
        try:
            validate(updates,schema)
            storage[id]=updates
            with open("mock_api/jsons/data_storage/update.json","w") as u:
                json.dump(storage,u,indent=4)
            return (200,{},json.dumps(storage[id]))
        except:
            return (422,{},json.dumps({"error":"invalid field"}))
    return (404,{},json.dumps({"error":"id is not valid"}))
def delete(request,storage=None):
    id=request.url.split("/")[-1]
    if id in storage:
        del storage[id]
        with open("mock_api/jsons/data_storage/delete.json", "w") as d:
            json.dump(storage,d,indent=4)
        return (200,{},json.dumps({"message":f"deleted id {id}"}))
    else:
        return (404,{},json.dumps({"error":"invalid id"}))
    