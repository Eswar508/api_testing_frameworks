import requests as rq
from utils.routes import Routes as R
def login_client(data):
    lr=rq.post(R.Log,json=data)
    return lr
def register_client(data):
    lr=rq.post(R.SgnUp,json=data)
    return lr