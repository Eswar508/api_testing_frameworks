from utils.logger import logger as log
import allure,json
class base_session:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.log=log()
    def end_point(self, route):
        self.log.info(f"_________API endpoint pointed to {route}_________")
        self.url=self.base_url+route
    def generate_token(self, data):
        self.log.info(f"getting token with data : {data}")
        allure.attach(body=json.dumps(data,indent=4),name="data",attachment_type=allure.attachment_type.JSON)
        allure.attach(body=f"the data is {json.dumps(data)}",name="data",attachment_type=allure.attachment_type.JSON)
        result=self.session.post(self.url, json=data)
        try:
            self.log.info(f"generated token : {result.json()["token"]} for status code : {result.status_code}")
        except:
            self.log.info(f"failed token generation with status code : {result.status_code}")
        return result
    def set_token(self, token):
        self.session.headers.update({'Cookie': f'token={token}'})
    def create_booking(self, data, headers=None):
        return self.session.post(self.url, json=data, headers=headers)
    def get_booking(self,id=None,headers=None):
        if id:
            url=self.url+f"/{id}"
        else:
            url=self.url
        return self.session.get(url, headers=headers)
    def update_booking(self, id, data, headers=None):
        url=self.url+f"/{id}"
        print(headers," is the headers")
        return self.session.put(url, json=data, headers=headers)
    def delete_booking(self, id):
        url=self.url+f"/{id}"
        return self.session.delete(url)
    def partial_update_booking(self, id, data, headers=None):
        url=self.url+f"/{id}"
        return self.session.patch(url, json=data, headers=headers)
    def get_token(self):
        try:return self.session.headers["Cookie"]
        except:
            print("Token not found in headers")
            return None