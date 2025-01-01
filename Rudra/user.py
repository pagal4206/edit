from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]
groups_collection = db["groups"]

def get_user_count():
    return users_collection.count_documents({})

def get_group_count():
    return groups_collection.count_documents({})

def add_user(user_id):
    if users_collection.count_documents({"user_id": user_id}) == 0:
        users_collection.insert_one({"user_id": user_id})

def add_group(group_id):
    if groups_collection.count_documents({"group_id": group_id}) == 0:
        groups_collection.insert_one({"group_id": group_id})