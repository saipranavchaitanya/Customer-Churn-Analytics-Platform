from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# PostgreSQL Connection URL
DATABASE_URL = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Debugging
print("DB_HOST =", DB_HOST)
print("DB_PORT =", DB_PORT)
print("DB_NAME =", DB_NAME)
print("DB_USER =", DB_USER)
print("DB_PASSWORD =", DB_PASSWORD)
print("DATABASE_URL =", DATABASE_URL)

# SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}
)