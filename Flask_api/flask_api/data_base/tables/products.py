from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Integer,Float,Boolean,ForeignKey
from flask_api.data_base.tables.base import Base
class Product(Base):

    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)

    name: Mapped[str] = mapped_column(String(100),nullable=False,unique=True)

    price: Mapped[float] = mapped_column(Float,nullable=False)

    stock: Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    category_id:Mapped[int]=mapped_column(ForeignKey("categories.category_id"),nullable=False)
    status: Mapped[bool] = mapped_column(Boolean,nullable=False)
    description: Mapped[str] = mapped_column(
    String(500),
    nullable=False
    )