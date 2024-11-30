import os
import urllib.parse
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_mongo_client():
    MONGO_USERNAME = os.getenv("MONGO_USERNAME") 
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")  
    
    encoded_username = urllib.parse.quote_plus(MONGO_USERNAME)
    encoded_password = urllib.parse.quote_plus(MONGO_PASSWORD)

    mongo_uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.q4305.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(mongo_uri)
    db = client.weather
    
    return db

# # Usage example
# db = get_mongo_client()

# # Example: Check if the connection is successful by listing collections
# print(db.list_collection_names())
