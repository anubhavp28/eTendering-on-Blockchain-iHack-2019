import pymongo
import requests
from pymongo import MongoClient
from profile_db import *


client = MongoClient()

db = client.users
user_collection = db.user_collection


profile = db.profile
user = {"dept_id":"",
		"dept_name":"",
		"dept_city":"",
		"dept_state":"",
		"dept_accno":publickey,
		"dept_secret":seed}
	
curr_user_id = profile.insert_one(user).inserted_id

