from flask_api.data_base.tables.products import Product
from flask_api.data_base.tables.users import User
from flask_api.data_base.tables.categories import Category
from flask_api.data_base.data_clients.session import engine
from flask_api.data_base.tables.base import Base
from flask_api.data_base.data_clients.data_factory import create_user,create_cat,product_factory
from flask_api.data_base.data_clients.session import SessionLocal
print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)
admin={"email":"admin@gmail.com","name":"admin","role":"admin","gender":"male"}
duplicate_product={"name":"geaser","price":99999999,"stock":99,"description":"this is updated","status":True,"category_id":1}
session=SessionLocal()
product_obj=product_factory(duplicate_product)
user_obj=create_user(**admin)
session.add(user_obj)
for i in range(1,4):
    obj=create_user(name=f"user{i}",email=f"user{i}@gmail.com")
    session.add(obj)
    co=create_cat(name=f"category{i}")
    session.add(co)
session.add(product_obj)
session.commit()
print("done")
