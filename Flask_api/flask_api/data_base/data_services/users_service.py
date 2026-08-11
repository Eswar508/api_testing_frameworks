from flask_api.data_base.tables.users import User
from flask_api.data_base.data_clients.session import SessionLocal
from flask_api.data_base.data_clients.helper_fun import user_dict
from flask_api.data_base.tables.users import User
from sqlalchemy import select
def get_user_by_email(email,to_dict=False):
    session=SessionLocal()
    stmt=select(User).where(User.email==email)
    r=session.scalars(stmt).first()
    return r
def get_user(**query):
    session=SessionLocal()
    stmt=select(User)
    for key,value in query.items():
        stmt=stmt.where(getattr(User,key)==value)
    r=session.scalars(stmt).first()
    return r