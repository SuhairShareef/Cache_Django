from pymongo import MongoClient


def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(
        "mongodb+srv://suhairshareef:ARoqg4EWwkGOLAZe@cluster0.m0ojcry.mongodb.net/"
    )
    db_handle = client[db_name]
    return db_handle, client


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]
