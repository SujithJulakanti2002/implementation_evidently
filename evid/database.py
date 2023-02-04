import json
import pymongo
from datetime import datetime

def func():
    # Connect to the database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]

    # Read the JSON file
    with open("json_file.json") as file:
        data_string = file.read()

    # Parse the JSON string into a dictionary
    data = json.loads(data_string)

    # Add the timestamp to the data
    data["timestamp"] = str(datetime.now())

    # Insert the data into the database
    collection.insert_one(data)
    
    print('\n\nJSON file is successfully pushed into the database!\n\n')
