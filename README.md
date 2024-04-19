# User CRUD operations with PyMongo

This repository contains Python code for performing CRUD (Create, Read, Update, Delete) operations on a user collection in MongoDB.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python3
- MongoDB
- Pip (Python installer package)

### Installation

Clone this repository

```
git clone https://github.com/pendragonarthur/python-user-crud.git
```

Navigate to the project directory

```
cd python-user-crud
```

Create and activate a virtual environment

On Windows:
```
python -m venv venv
.venv\Scripts\activate
```

On Linux/macOS

```
python3 -m venv venv
source venv/bin/activate
```

Install all dependencies
```
pip install -r requirements.txt
```

## Usage

1. Ensure your MongoDB server is running
2. Set up a .env file in the root directory of the project with your MongoDB connection string.
3. Run the python script

```
python app.py
```
4. To perform the CRUD operations, make sure to call the desired function

Example (if you want to test the create function):

```
######
app.py code here
###### 

create_user()
```

### Functions

- create_user(): Create a new user document in the collection.
- get_user_by_username(): Retrieve a user document by providing the username.
- get_all_users(): Retrieve all user documents in the collection.
- delete_user_by_username(): Delete a user document by providing the username.
- update_user_by_username(): Update a user document by providing the username and selecting the field to update.

## Built With

* [Python](https://www.python.org/downloads/) - Programming language used
* [Pip] - Dependency Management
* [MongoDB](https://www.mongodb.com) - No relational database 
* [Pymongo](https://pymongo.readthedocs.io/en/stable/) - Python driver for MongoDB
* [Python-dotenv](https://pypi.org/project/python-dotenv/) - Environment managing library
