from testing_framework.clients.product_client import post_product
data={"name":"geaser","price":99999,"stock":99,"description":"this is updated","status":True,"category_id": 1}
r=post_product(data)
from config import DATABASE_URL
from flask_api.data_base.data_clients.data_factory import product_factory
from flask_api.data_base.data_clients.session import SessionLocal
p=product_factory(data)
session=SessionLocal()
session.add(p)
session.commit()
