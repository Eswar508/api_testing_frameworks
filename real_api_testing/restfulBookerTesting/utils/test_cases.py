from utils.data_loader import data_loader
from utils.routes import Routes
import time
import requests
class test_cases:
    booking_url=Routes.base_url+Routes.booking
    loging_url=Routes.base_url+Routes.login
    session=requests.session()
    @classmethod
    def booking(cls):
        return data_loader("Test_cases/booking/valid_data.json")
    @classmethod
    def booked_data(cls):
        load=data_loader("Test_cases/booking/booked_data.json")
        cls.session.post(cls.booking_url,json=load)
        time.sleep(1)
        return load
    @classmethod
    def invalid_booking(cls):
        return data_loader("Test_cases/booking/invalid_data.json")
    @classmethod
    def get(cls):
        load=data_loader("Test_cases/get_data.json")
        print(load)
        Ids=[]
        data=[]
        for i in load:
            response=cls.session.post(cls.booking_url,json=i).json()
            id=response["bookingid"]
            D=response["booking"]
            Ids.append(id)
            data.append(D)
            time.sleep(1)
        return zip(Ids,data)
    @classmethod
    def delete(cls):
        load=data_loader("Test_cases/delete/data.json")
        Ids=[]
        for _ in load:
            response=cls.session.post(cls.booking_url,json=_).json()
            id=response["bookingid"]
            Ids.append(id)
            time.sleep(1)
        return Ids
    @classmethod
    def deleted0(cls):
        load=data_loader("Test_cases/delete/deleted0_data.json")
        print(load," is the load")
        response=cls.session.post(cls.booking_url,json=load).json()
        id=response["bookingid"]
        print(id," is the post response")
        r=cls.session.delete(cls.booking_url+"/"+str(id))
        print(r.status_code," is the deleted response")
        time.sleep(1)
        return id
    @classmethod
    def deleted1(cls):
        load=data_loader("Test_cases/delete/deleted1_data.json")
        print(load," is the load")
        response=cls.session.post(cls.booking_url,json=load).json()
        id=response["bookingid"]
        print(id," is the post response")
        r=cls.session.delete(cls.booking_url+"/"+str(id))
        print(r.status_code," is the deleted response")
        time.sleep(1)
        return id
    @classmethod
    def update(cls):
        load=data_loader("Test_cases/edit/update_ids.json")
        id=cls.session.post(cls.booking_url,json=load).json()["bookingid"]
        return id
    @classmethod
    def partial_update(cls):
        load=data_loader("Test_cases/edit/partial_update_ids.json")
        id=cls.session.post(cls.booking_url,json=load).json()["bookingid"]
        return id
    @classmethod
    def auth_put(cls):
        load=data_loader("Test_cases/auth/put_token.json")
        test_cases=[]
        for L in load:
            id=cls.session.post(cls.booking_url,json=L["data"]).json()["bookingid"]
            if L["header"]=="":
                L["header"]=None
            test_cases.append({"id":id,"expected_code":L["expected_code"],"header":L["header"]})
        return test_cases
    @classmethod
    def auth_post(cls):
        load=data_loader("Test_cases/auth/post_token.json")
        test_cases=[]
        for L in load:
            if L["header"]=="":
                L["header"]=None
            L["expected_code"]=int(L["expected_code"])
            test_cases.append(L)
        return test_cases
    @classmethod
    def login(cls):
        load=data_loader("Test_cases\login\data.json")
        return load
    @classmethod
    def invalid_login(cls):
        load=data_loader("Test_cases\login\invalid_data.json")
        return load
    @classmethod
    def put_data(cls):
        load=data_loader("Test_cases\edit\put_data.json")
        return load