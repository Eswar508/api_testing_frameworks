from marshmallow import Schema,fields,validate
class ProductSchema(Schema):
    name=fields.String(required=True,validate=validate.Length(min=3,max=50))
    price=fields.Float(required=True)
    stock=fields.Integer(required=True)
    category_id=fields.Integer(required=True)
    status=fields.Boolean(required=True)
    description=fields.String(required=True,validate=validate.Length(min=6,max=100))
class LoginSchema(Schema):
    email=fields.Email(required=True)
    password=fields.String(required=True,validate=validate.Regexp(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,20}$"))
class token_data_schema(Schema):
    user_id=fields.Integer(required=True)
    iat=fields.Integer(required=True)
    exp=fields.Integer(required=True)
    role=fields.String(validate=validate.OneOf(["admin","staff"]),required=True)