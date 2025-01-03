from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]
groups_collection = db["groups"]

def add_user(user_id):
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id})
        print(f"User added: {user_id}")

def add_group(group_id):
    if not groups_collection.find_one({"group_id": group_id}):
        groups_collection.insert_one({"group_id": group_id})
        print(f"Group added: {group_id}")

def get_user_count():
    return users_collection.count_documents({})

def get_group_count():
    return groups_collection.count_documents({})

def get_all_users():
    return [user["user_id"] for user in users_collection.find()]

def get_all_groups():
    return [group["group_id"] for group in groups_collection.find()]