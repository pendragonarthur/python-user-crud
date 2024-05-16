from pymongo import MongoClient
from dotenv import load_dotenv
import os
import requests

load_dotenv()

connection = os.getenv("CONNECTION_STRING")

client = MongoClient(connection)

db = client["user_db"]
collection = db.user_collection
address_collection = db.address_collection

def create_user():
    
    try:
        username = str(input("Insert your username: "))
        email = str(input("Insert your best email: "))
        age = int(input("Insert your age: "))
        zip_code = input("Insert your Zip Code: ")

        response = requests.get(f"https://viacep.com.br/ws/{zip_code}/json/")

        if response.status_code == 200:
            address_info = response.json()
            address = {
                "street": address_info.get("logradouro", ""),
                "city": address_info.get("localidade", ""),
                "zipcode": address_info.get("cep", ""),
                "state": address_info.get("uf", ""),
                "country": address_info.get("pais", "")
            }
        else:
            print("Failed to find zip code.")
            return

        address["owner"] = username

        user = {
            "username": username, 
            "email": email, 
            "age": age,
            "address": address
        }

        created_user = collection.insert_one(user)
        print("User created successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

def get_user_by_username():
    try:
        user = str(input("Insert the username to be listed: "))

        result = collection.find_one({"username": user})
        
        if result is not None:
            print(result)
        else:
            print(f"{user} not found.")

    except Exception as e:
        print(f"Error: {e}")

def get_all_users():
    try:
        result = collection.find()

        if result is None:
            print("No users found.")
        else:
            for user in result:
                print(user)

    except Exception as e:
        print(f"Error: {e}")

def delete_user_by_username():
    try:
        user = str(input("Inser the username to be deleted: ")) 
        result = collection.delete_one({"username": user})

        if result is not None:         
            print("User deleted successfully.")
        else: 
            print(f"{user} not found.")
    
    except Exception as e:
        print(f"Error: {e}")

def update_user_by_username():
    try:
        user = str(input("Insert the username to be updated: "))

        option = input("Insert the field to be updated (username, email, age): ")

        match option:
            case "username":
                new_user = str(input("Insert the updated username: "))
                result = collection.update_one({"username": user}, {"$set": {"username": new_user}})
                if user is None:
                    print(f"{user} not found.")
                else:
                    print(f"{user}'s user updated. New user: {new_user}") 
            
            case "age":
                new_age = int(input("Insert the updated age: "))
                result = collection.update_one({"username": user}, {"$set": {"age": new_age}})
                if user is None:
                    print(f"{user} not found.")
                else:
                    print(f"{user}'s age updated. New age: {new_age}")                 

            case "email":
                new_email = str(input("Insert the updated email: "))
                result = collection.update_one({"username": user}, {"$set": {"email": new_email}})
                if user is None:
                    print(f"{user} not found.")
                else:
                    print(f"{user}'s email updated. New email: {new_email}") 


    except Exception as e:
        print(f"Error: {e}")

get_user_by_username()