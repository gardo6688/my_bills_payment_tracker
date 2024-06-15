from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.my_bills_payment_tracker  # Replace with your database name
