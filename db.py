import os

import pymongo
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(
    f'mongodb+srv://{os.getenv("DB_USER")}:{os.getenv("DB_USER_PASSWORD")}@cluster0.eoife.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.new_pravo_help
requests_collection = db.requests
users_collection = db.users


class DB:
    def insert_request(self, service, service_option, form_time, cad_obj):
        requests_collection.insert_one({
            'service': service,
            'service_option': service_option,
            'form_time': form_time,
            'cad_obj': cad_obj})

    def insert_user(self, tg_id, username, first_name, last_name):
        users_collection.insert_one({
            'tg_id': tg_id,
            'username': username,
            'first_name': first_name,
            'last_name': last_name})

    def find_user_by_tg_id(self, tg_id):
        return users_collection.find_one({'tg_id': tg_id})
