from jsonschema import validate,ValidationError
from utils.log import log
class FedSession:
    def __init__(self,session,url,schema):
        self.session=session
        self.url=url
        self.schema_list=schema
    def method_result(self,method,expected_code:int,schema=None,data={},id=None,return_only_bool=False):
        if id ==None:
            id=""
        else:
            id="/"+str(id)
        r=None
        if method=="POST":
            r=self.session.request(method,f"{self.url}/users",json=data)
        elif method=="GET":
            r=self.session.request(method,f"{self.url}/users{id}",params=data)
            print(f"{self.url}/users{id}")
            print()
        elif method == "PATCH":
            r=self.session.request(method,f"{self.url}/users{id}",json=data)
        elif method == "PUT":
            r=self.session.request("PUT",f"{self.url}/users{id}",json=data)
        elif method =="DELETE":
            r=self.session.request("DELETE",f"{self.url}/users{id}")
            return True if r.status_code == expected_code else False
        else:
            return
        Log=log()
        Log.info(f"response code is {r.status_code}")
        B={"status_code":False,"json_formate":False}
        id=None
        try:
            id=r.json()["id"]
        except:
            pass
        #validating test result
        try:
            s=self.schema_list[schema]
            validate(r.json(),s)
            B["json_formate"]=True
        except:
            pass
        if r.status_code == expected_code:
            B["status_code"]=True
        print(r.json())
        print()
        print(r.status_code)
        if return_only_bool:
            print()
            print()
            print(id,B)
            return True if B["status_code"] and B["json_formate"] else False
        return id,B
    def create_user(self,data):
        r=self.session.post(f"{self.url}/users",json=data)
        return r
    def patch(self,id,data):
        r=self.session.patch(f"{self.url}/users/{id}",json=data)
        return r
    def put(self,id,data):
        r=self.session.put(f"{self.url}/users/{id}",json=data)
        return r