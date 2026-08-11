import requests
from testing_framework.utils.helper_fun import new_token,session
def get_header_if_token(token):
    header=None
    if token != None: header={"Authorization":f"Bearer {token}"}
    return header
def get_product(id,token=None):
    header=get_header_if_token(token)
    r=session.get(f"http://127.0.0.1:5000/product/get/{id}",headers=header)
    return r
def get_products(token=None,**query):
    header=get_header_if_token(token)
    r=session.get(f"http://127.0.0.1:5000/product/get",params=query,headers=header)
    return r
def post_product(data,token=None):
    header=get_header_if_token(token)
    r=session.post(f"http://127.0.0.1:5000/product/post",json=data,headers=header)
    return r
def patch_product(id,data,token=None):
    header=get_header_if_token(token)
    r=session.patch(f"http://127.0.0.1:5000/product/patch/{id}",json=data,headers=header)
    return r
def update_product(id,data,token=None):
    header=get_header_if_token(token)
    r=session.put(f"http://127.0.0.1:5000/product/put/{id}",json=data,headers=header)
    return r
def delete_product(id,token=None):
    header=get_header_if_token(token)
    r=session.delete(f"http://127.0.0.1:5000/product/delete/{id}",headers=header)
    return r