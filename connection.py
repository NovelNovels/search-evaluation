from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os


def connect_mongodb():
    load_dotenv(find_dotenv())

    uri = os.environ.get("MONGO_URI")
    user = os.environ.get("USERNAME")
    password = os.environ.get("PSWD")

    client = MongoClient(uri, username=user, password=password)

    db = client.BookSearch
    books = db.current_test_data

    try:
        db.command('ping')
        print('Connected to MongoDB.')
    except:
        raise Exception('Cannot connect to MongoDB.')

    return books
