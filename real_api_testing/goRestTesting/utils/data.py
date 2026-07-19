import json
def data(s):
    with open(s,"r") as f:
        j=json.load(f)
    return j