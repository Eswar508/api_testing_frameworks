from flask_api.data_base.tables.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Enum,String
class User(Base):
    __tablename__="users"
    user_id: Mapped[int] = mapped_column(primary_key=True,nullable=False,autoincrement=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    email:Mapped[str] =mapped_column(String(100),nullable=False,unique=True)
    role:Mapped[str] = mapped_column(
    Enum("admin", "staff", name="role_enum"),
    nullable=False
)
    gender:Mapped[str]=mapped_column(Enum("male","female","other",name="gender_enum"),nullable=False)
