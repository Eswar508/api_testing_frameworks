from flask import Blueprint,request
from flask_api.api_client import *
from flask_api.helper_fun import validate_product_schema,validate_patch_schema,allowed_for_only_admins
product_bp=Blueprint("product",__name__,url_prefix="/product")
@product_bp.get("/get")
def get_products():
    params=request.args.to_dict()
    return get_prods(params)
@product_bp.get(f"/get/<int:id>")
def get_product(id):
    return get_prod(id)
@product_bp.post("/post")
@allowed_for_only_admins
def post_product():
    product_request=request.json
    product,error=validate_product_schema(product_request)
    if error:
        return error,422
    response=post_prod(product)
    return response
@product_bp.patch("/patch/<int:id>")
@allowed_for_only_admins
def patch_product(id):
    product_request=request.json
    product,error=validate_patch_schema(product_request)
    if error:
        return error,422
    response=patch_prod(id,product)
    return response
@product_bp.put("/put/<int:id>")
@allowed_for_only_admins
def update_product(id):
    product_request=request.json
    product,error=validate_product_schema(product_request)
    if error:
        return error,422
    response=update_prod(id,product)
    return response
@product_bp.delete("/delete/<int:id>")
@allowed_for_only_admins
def delete_product(id):
    response=delete_prod(id)
    return response