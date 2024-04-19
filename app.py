from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

connection = os.getenv("CONNECTION_STRING")

client = MongoClient(connection)

# Creating DB

db = client["user_db"]
collection = db.user_collection

# Create user function with user input

def create_user():
    try:
        username = str(input("Insert your username: "))
        email = str(input("Insert your best email: "))
        age = int(input("Insert your age: "))

        user = {
            "username": username, 
            "email": email, 
            "age": age
        }

        collection.insert_one(user)
        print("User created successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

# Calling create user function:
# create_user()

def get_users_by_username(person_id):
    try:
        search = str(input("Insert the username: "))

        result = collection.find_one({"username": search})
        
        if result is not None:
            print(result)
        else:
            print(f"{search} not found.")

    except Exception as e:
        print(f"Error: {e}")

