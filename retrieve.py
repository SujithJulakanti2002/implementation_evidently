import pymongo
from datetime import datetime, timedelta

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]
collection = db["mycollection"]

# Define the start and end timestamps for the range
start_timestamp = input('Enter the end timestamp [format is yyyy-mm-dd hh:mm:ss]: ')
end_timestamp = input('Enter the end timestamp [format is yyyy-mm-dd hh:mm:ss]: ')

# Query the collection for documents within the timestamp range
results = collection.find({"timestamp": {"$gte": start_timestamp, "$lte": end_timestamp}})

# initializing lists for drift score and timestamp
drift_score = []
timestamp = []

# Iterate through the results and print each document
for document in results:
    print(document)
    timestamp.append(document['timestamp'])
    drift_score.append(document['metrics'][2]['result']['drift_score'])

# print(timestamp)
# print(drift_score)

# Close the MongoDB connection
client.close()


