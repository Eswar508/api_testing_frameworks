from utils.assertions import validate
def Test_response(values,Post_method=False):
    assert_True=validate(values.response)
    print(values.response.status_code," is the status_code and ",values.code," is the expected status code")
    assert_True.if_status_code(values.code) if values.code is not None else None
    if values.data and values.code ==200:
        assert_True.if_booking_data_matches(values.data)
        assert_True.if_id_is_int() if Post_method else None