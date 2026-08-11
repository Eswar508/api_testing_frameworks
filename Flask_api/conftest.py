import pytest
from flask_api.data_base.data_clients.session import SessionLocal
from flask_api.data_base.data_clients.data_factory import product_factory,create_user
from flask_api.data_base.tables.products import Product
pytest_plugins = [
    "testing_framework.fixtures.token_fixtures",
    "testing_framework.fixtures.product_fixtures",
]
@pytest.fixture(scope="function")
def session():
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()
@pytest.fixture(scope="function")
def prod_factory(session):
    created=[]
    def add_prod(**kwargs):
        p=product_factory(kwargs)
        session.add(p)
        session.commit()
        created.append(p)
        return p
    try:
        yield add_prod
    finally:
        for p in created:
            pd=session.get(Product,p.product_id)
            if pd:
                session.delete(p)
    session.commit()
    