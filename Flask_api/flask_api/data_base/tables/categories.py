from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Integer,ForeignKey
from flask_api.data_base.tables.base import Base
class Category(Base):
    __tablename__="categories"
    category_id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(String(100),nullable=False)