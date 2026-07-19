import requests,time,os
import json
from jsonschema import validate,ValidationError
from utils.data import data as load_data
s=requests.session()
API="https://gorest.co.in/public/v2"
token="6c5909f00d0b785d5cdc4514ee20960d7c67a8951c1001ccf1b6421e0f1a8b1a"
s.headers.update({
        "Authorization":f"Bearer {token}",
        "Accept":"application/json",
        "Content-Type":"application/json",
    })
payload={"name":"djndjdf",
         "email":"kjdnf@gmail.com",
         "gender":"male",
         }
#'X-Ratelimit-Limit': '300', 'X-Ratelimit-Remaining': '299', 'X-Ratelimit-Reset': '0',
for i in range(1,340):
    r=s.get(F"{API}/users/8516014")
    print(f"{i} -> {r.status_code} -> {r.headers['X-Ratelimit-Limit']} -> {r.headers['X-Ratelimit-Remaining']} -> {r.headers['X-Ratelimit-Reset']}")