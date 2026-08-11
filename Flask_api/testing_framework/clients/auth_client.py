import requests
def login_client(login_data):
    response=requests.post("http://127.0.0.1:5000/login",json=login_data)
    return response
    