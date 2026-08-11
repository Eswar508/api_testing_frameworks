from sqlalchemy.exc import IntegrityError

from flask_api.data_base.data_clients.data_factory import product_factory
from flask_api.data_base.tables.products import Product
from flask_api.data_base.data_clients.helper_fun import to_dict
from flask_api.data_base.data_clients.session import SessionLocal
from sqlalchemy import select
def get_products(query_data,session):
    try:
        stmt=select(Product)
        for field,value in query_data.items():
            stmt=stmt.where(getattr(Product,field)==value)
        prods=session.scalars(stmt).all()
        r=[]
        if not prods:return None
        for p in prods:
            r.append(to_dict(p))
        return r
    except Exception:
        raise
def get_product(id,session):
    try:
        r=session.get(Product,id)
        if not r: return None
        return to_dict(r)
    except Exception:
        session.rollback()
        raise
def insert_product(product_data,session):
    try:
        p=product_factory(product_data)
        session.add(p)
        session.commit()
        return to_dict(p)
    except IntegrityError:
        session.rollback()
        return "duplicate fields found"
    except Exception:
            session.rollback()
            raise
def update_product(product_id,product_data,session):
    try:
        p=session.get(Product,product_id)
        if not p : return None
        for key,value in product_data.items():
            setattr(p,key,value)
        session.commit()
        return to_dict(p)
    except IntegrityError:
        session.rollback()
        return "duplicate fields found"
    except Exception:
            session.rollback()
            raise
def delete_product(product_id,session):
    try:
        prod=session.get(Product,product_id)
        if not prod : return None
        session.delete(prod)
        session.commit()
        return True
    except Exception:
            session.rollback()
            raise