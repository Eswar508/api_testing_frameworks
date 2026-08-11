from flask_api.data_base.tables.products import Product
from flask_api.data_base.tables.users import User
from flask_api.data_base.tables.categories import Category
from flask_api.data_base.tables.users import User
from flask_api.data_base.data_clients.helper_fun import to_dict
def product_factory(product_data:dict|None={}):
    product=Product(
        name="Laptop",
        price=40000,
        stock=150,
        status=True,
        category_id=1,
        description="designed for college studentds and watching movies"
    )
    for key,value in product_data.items():
        setattr(product,key,value)
    return product
def create_cat(**kwargs):
    category=Category(
        name="electronics"
    )
    for key,value in kwargs.items():
        setattr(category,key,value)
    return category

    
def create_user(**kwargs):
    user=User(
        name="user1",
        email="user1@gmail.com",
        role="staff",
        gender="male"
    )
    if "name" in kwargs:
        user.email=kwargs["name"]+"@gmail.com"
    for key,value in kwargs.items():
        setattr(user,key,value)
    return user

























"""@pytest.fixture
def db_session():

    session = SessionLocal()

    transaction = session.begin()

    yield session

    transaction.rollback()

    session.close()"""