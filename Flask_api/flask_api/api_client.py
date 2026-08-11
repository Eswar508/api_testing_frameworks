from flask_api.data_base.data_services.product_services import *
from flask_api.data_base.data_clients.session import SessionLocal
from flask import jsonify
from functools import wraps
def get_prod(id):
    session=SessionLocal()
    try:
        product=get_product(id,session)
        if product is None:
            return {"message": "Product not found"}, 404
        return jsonify(product),200
    except Exception:
        return {"message":"internal server error"},500
    finally:
        session.close()
def get_prods(query_data):
    session=SessionLocal()
    try:
        prods=get_products(query_data,session)
        if prods:
            return jsonify(prods),200
        return {"message": "Product not found"}, 404
    except Exception:
            return {"message":"internal server error"},500
    finally:
        session.close()
def post_prod(product_data):
    session=SessionLocal()
    try:
        prod=insert_product(product_data,session)
        if prod == "duplicate fields found":
            return {"message": "duplicate fields found"}, 403
        return jsonify(prod),201
    except Exception:
            return {"message":"internal server error"},500
    finally:
        session.close()
def update_prod(product_id,product_data):
    session=SessionLocal()
    try:
        prod=update_product(product_id,product_data,session)
        if prod == None:
            return {"message": "Product not found"}, 404
        if prod == "duplicate fields found":
            return {"message": "duplicate fields found"}, 403
        return jsonify(prod),200
    except Exception:
            return {"message":"internal server error"},500
    finally:
        session.close()
def patch_prod(product_id,product_data):
    session=SessionLocal()
    try:
        prod=update_product(product_id,product_data,session)
        if prod == None:
            return {"message": "Product not found"}, 404
        if prod == "duplicate fields found":
            return {"message": "duplicate fields found"}, 403
        return jsonify(prod),200
    except Exception:
                return {"message":"internal server error"},500
    finally:
        session.close()
def delete_prod(product_id):
    session=SessionLocal()
    try:
        r=delete_product(product_id,session)
        if r == None:
            return {"message": "Product not found"}, 404
        return {"message":f"deleted product with id {product_id}"},204 
    except Exception:
        return {"message":f"couldn't delete the product with id {product_id}"},404