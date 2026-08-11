import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("JWT_ALGORITHM","HS256")
JWT_EXPIRY_HOURS=int(os.getenv("JWT_EXPIRY_HOURS","1"))
DATABASE_URL=os.getenv("DATABASE_URL")