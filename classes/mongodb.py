from pymongo import MongoClient
import pymongo


class MongoDB:
    def __init__(self, uri):
        self.uri = uri

    def get_database(self):
        client = MongoClient(self.uri)
        return client['application_database'] 

    def user_exists(self, user_id):
        db = self.get_database()
        users = db['users']

        return users.find_one({'user_id': user_id})    

    def add_user(self, user_data):
        db = self.get_database()
        users = db['users']

        users.insert_one(user_data)   

    def subscribe_user(self, user_id):
        db = self.get_database()
        users = db['users']

        users.update_one({'user_id': user_id}, {'$set': {'status': True}})

    def unsubscribe_user(self, user_id):
        db = self.get_database()
        users = db['users']

        users.update_one({'user_id': user_id}, {'$set': {'status': False}})

    def get_subscriber(self, user_id):
        db = self.get_database()
        users = db['users']

        return users.find_one({'user_id': user_id, 'status': True}) 

    def get_subscribers(self):
        db = self.get_database()
        users = db['users']

        return users.find({'status': True})

