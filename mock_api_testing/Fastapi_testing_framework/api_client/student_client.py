import requests as rq
from utils.routes import Routes as R
def headers(token):
    return {"Authorization": f"Bearer {token}"} if token else {}
def get_student_account(token : str|None=None,id :int | None=None):
    getR=None
    if id:
        getR=rq.get(R.StuId+str(id),headers=headers(token))
    else:
        getR=rq.get(R.StuSelf,headers=headers(token))
    return getR
def update_student_account(token :str,payload: dict,id : int| None=None):
    ur=None
    if id:
        ur=rq.put(R.StuId+str(id),json=payload,headers=headers(token))
    else:
        ur=rq.put(R.StuSelf,json=payload,headers=headers(token))
    return ur
def patch_student_account(token :str,payload: dict,id : int| None=None):
    pr=None
    if id:
        pr=rq.patch(R.StuId+str(id),json=payload,headers=headers(token))
    else:
        pr=rq.patch(R.StuSelf,json=payload,headers=headers(token))
    return pr
def delete_student_account(token :str,id :int| None=None):
    dr=None
    if id:
        dr=rq.delete(R.StuId+str(id),headers=headers(token))
    else:
        dr=rq.delete(R.StuSelf,headers=headers(token))
    return dr
