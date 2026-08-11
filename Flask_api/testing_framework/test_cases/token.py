import datetime
import jwt
expired_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpYXQiOjE3ODUxNDg4NTUsImV4cCI6MTc4NTE1MjQ1NSwicm9sZSI6InN0YWYifQ.jiKou_u4To-Ge9tpwa1B7XzUOI-LdPzYoECaR_9Pgi0'
def genereate_invalid_signature_token(token):
    parts=token.split(".")
    parts[-1]="invalidsignature"
    return ".".join(parts)
from flask_api.helper_fun import generate_token
def generate_tampered_token(token):
    tampered_payload_part=generate_token("adminX",3).split(".")[1]
    parts=token.split(".")
    parts[1]=tampered_payload_part
    return ".".join(parts)
malformed_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpYXQiOjE3ODUxNDg4NTUsImV4cCI6MTc4NTE1MjQ1NSwicm9sZSI6InN0YWYifQ'
def generate_wrong_algorithm_token():
    role="admin"
    id=1
    payload={
    "user_id":id,
    "iat":datetime.datetime.now(datetime.timezone.utc),
    "exp":datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=1),
    "role":role
    }
    SECRET_KEY="My_Secrete_Token_Key_Which_Is_32_Bytes_Long"
    ALGORITHM="HS384"
    Token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return Token