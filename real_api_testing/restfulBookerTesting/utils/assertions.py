class validate:
    def __init__(self,response):
        self.response=response
        try: self.json=response.json()
        except ValueError: self.json={}
        self.status_code=response.status_code
    def if_token_is_string(self):
        #first check if 'token' is present in the response json, then check if it's a string
        assert self.json
        assert 'token' in self.json
        assert isinstance(self.json.get('token'), str)
    def if_status_code(self, expected_code):
        assert self.status_code == expected_code    
    def if_token_is_not_present(self):
        assert 'token' not in self.json
    def if_id_is_int(self):
        assert 'bookingid' in self.json
        assert isinstance(self.json.get('bookingid'), int)
    def if_booking_data_matches(self, expected_data):
        if "booking" not in self.json:
            response_data=self.json
            print(response_data," is response data")
            print(expected_data," is expected data")
            assert response_data==expected_data
        else:
            response_data=self.json.get('booking')
            assert response_data==expected_data