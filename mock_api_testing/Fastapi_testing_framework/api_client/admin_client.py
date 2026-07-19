import requests as rq
from utils.routes import Routes as R
def headers(token):
    return {"Authorization": f"Bearer {token}"} if token else {}
def get_admin_account(token : str|None=None,id :int | None=None):
    getR=None
    if id:
        getR=rq.get(R.AdmID+str(id),headers=headers(token))
    else:
        getR=rq.get(R.AdmsSelf,headers=headers(token))
    return getR
def update_admin_account(token :str,payload: dict):
    ur=rq.put(R.AdmsSelf,json=payload,headers=headers(token))
    return ur
def patch_admin_account(token :str,payload: dict):
    pr=rq.patch(R.AdmsSelf,json=payload,headers=headers(token))
    return pr