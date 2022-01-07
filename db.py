import os

import pymongo
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

client = pymongo.MongoClient(
    f'mongodb+srv://{os.getenv("DB_USER")}:{os.getenv("DB_USER_PASSWORD")}@cluster0.eoife.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.new_pravo_help
requests_collection = db.requests
users_collection = db.users

requests_counter = 0


class DB:
    def insert_request(self, info_from_message, service, service_option, form_time, cad_obj):
        global requests_counter
        requests_counter += 1
        requests_collection.insert_one({
            'request_id': requests_counter,
            'client': {
                'tg_id': info_from_message['from']['id'],
                'username': info_from_message['from']['username'],
                'first_name': info_from_message['from']['first_name'],
                'last_name': info_from_message['from']['last_name'],
            },
            'service': service,
            'service_option': service_option,
            'form_time': form_time,
            'cad_obj': cad_obj})

    def find_request_by_id(self, request_id):
        return requests_collection.find_one({'request_id': request_id})

    def insert_user(self, tg_id, username, first_name, last_name):
        users_collection.insert_one({
            'tg_id': tg_id,
            'username': username,
            'first_name': first_name,
            'last_name': last_name})

    def find_user_by_tg_id(self, tg_id):
        return users_collection.find_one({'tg_id': tg_id})
