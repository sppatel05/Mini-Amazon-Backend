from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["ecommerce_db"]

users_collection = db["users"]
products_collection = db["products"]
cart_collection = db["cart"]
orders_collection = db["orders"]
