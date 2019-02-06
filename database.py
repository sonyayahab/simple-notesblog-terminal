from pymongo import MongoClient

class Database(object):
    # These is the static properties or as the blueprint
    uri = 'mongodb://127.0.0.1:27017'
    database = None

    # We're not going to use self
    # You have to initialize first the collection that will be use on your Mongod
    # As example, my collection here named as fullstack
    @staticmethod
    def initialize():
        client = MongoClient(Database.uri)
        Database.database = client ['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.database[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.database[collection].find_one(query)
