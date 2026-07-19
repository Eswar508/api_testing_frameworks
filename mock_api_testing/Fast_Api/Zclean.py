import json
def get_data(path):
    with open(path) as f:
        return json.load(f)
def post_data(path,data):
    with open(path,"w") as f:
        json.dump(data,f,indent=5)
ids_path=r"FastApi\storage\user_ids.json"
password_path=r"FastApi\storage\user_passwords.json"
data_path=r"FastApi\storage\user_registry.json"
source_ids_path=r"clean_up\ids.json"
source_password_path=r"clean_up\password.json"
source_data_path=r"clean_up\registry.json"
def cleaner():
    id_storage=get_data(source_ids_path)
    password_storage=get_data(source_password_path)
    data_storage=get_data(source_data_path)
    print("on the way")
    post_data(ids_path,id_storage)
    post_data(password_path,password_storage)
    post_data(data_path,data_storage)

cleaner()
print("finishfed")