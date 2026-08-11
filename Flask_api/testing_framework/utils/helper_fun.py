from testing_framework.clients.auth_client import login_client
import requests
def new_token():
    payload={"email":"admin@gmail.com","password":"@User123"}
    r=login_client(payload)
    return r.json()["access_token"]
session=requests.Session()
session.headers["Authorization"]=f"Bearer {new_token()}"
