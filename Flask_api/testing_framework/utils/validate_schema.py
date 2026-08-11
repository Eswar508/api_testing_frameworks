from flask_api.schema_validation import ProductSchema,token_data_schema
from marshmallow import Schema,fields,validate
class ProductResponseSchema(ProductSchema):
    product_id=fields.Int(required=True)
class UserDict(Schema):
    user_id=fields.Int(required=True)
    name=fields.String(required=True)
    email=fields.Email(required=True)
class LoginResponseSchema(Schema):
    access_token=fields.String(required=True)
    token_type=fields.String(required=True)
    user=fields.Nested(UserDict,required=True)
def validate_login_schema(login_data):
    schema = LoginResponseSchema()
    try:
        schema.load(login_data)
        return True
    except:
        return False
def validate_product_schema(product):
    schema=ProductResponseSchema()
    try:
        schema.load(product)
        return True
    except:
        return False
def validate_token_schema(token_data):
    schema=token_data_schema()
    try:
        schema.load(token_data)
        return True
    except:
        return False