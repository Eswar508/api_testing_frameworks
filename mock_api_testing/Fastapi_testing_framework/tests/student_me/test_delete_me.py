from test_cases.student_data import StudentData
from api_client.student_client import delete_student_account
def test_student_delete_me():
    token=StudentData.delete_token2()
    delete_response=delete_student_account(token)
    assert delete_response.status_code==204
    assert "message" in delete_response.json()
def test_delete_student_by_deleted_token(deleted_token):
    delete_response=delete_student_account(deleted_token)
    assert delete_response.status_code==204
