import json
def data(path):
    with open(path) as f:
        D=json.load(f)
    return D
class Test_cases:
    @classmethod
    def post(cls):
        return data("mock_api/jsons/data_source/post.json")
    @classmethod
    def get(cls):
        return data("mock_api/jsons/data_source/get.json")
    @classmethod
    def patch(cls):
        return data("mock_api/jsons/data_source/patch.json")
    @classmethod
    def put(cls):
        return data("mock_api/jsons/data_source/put.json")
    @classmethod
    def delete(cls):
        return data("mock_api/jsons/data_source/delete.json")
class storage:
    @classmethod
    def get(cls):
        return data("mock_api/jsons/data_storage/get.json")
    @classmethod
    def patch(cls):
        return data("mock_api/jsons/data_storage/partial_update.json")
    @classmethod
    def put(cls):
        return data("mock_api/jsons/data_storage/update.json")
    @classmethod
    def delete(cls):
        return data("mock_api/jsons/data_storage/delete.json")
    @classmethod
    def schema(cls):
        return data("mock_api/jsons/json_schemas/schemas.json") 
    @classmethod
    def schema_field(cls):
        return data("mock_api/jsons/json_schemas/schema_put.json")

def get_id(url="mock_api/jsons/data_source/get_id.json"):
    ids=data(url)
    id=ids.pop()
    with open(url,"w") as f:
        json.dump(ids,f)
    return id