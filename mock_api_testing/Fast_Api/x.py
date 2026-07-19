from testing_framework.utils.helper_fun import get_token_data
token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpYXQiOjE3ODQzOTI3NTEsImV4cCI6MTc4NDM5NjM1MSwicm9sZSI6ImFkbWluIn0.cjPmNSlSNdXB88rxvW9G8mJPlNCMJQFNoFnodomp840"
print(get_token_data({"email":"admin1@gmail.com","password":"$AnAdmin1"}))