from dotenv import find_dotenv, load_dotenv
import os

find_dotenv()
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("HOST")
DB_PORT = os.getenv("DB_PORT")

SECRET_KEY = "GPs9BTxhRInS6nz62MOzxr"

DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
