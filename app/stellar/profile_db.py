import pymongo
import datetime
import requests
from stellar_base.builder import Builder
from stellar_base.address import Address
from pymongo import MongoClient
from stellar_base.utils import StellarMnemonic
from stellar_base.keypair import Keypair


client = MongoClient()

db = client.users
user_collection = db.user_collection

#secret is the phrase so user does not has to enter both
#public and private key
sm = StellarMnemonic("english")
secret = sm.generate()
kp = Keypair.deterministic(secret, lang="english", index=1)
publickey = kp.address().decode()
seed = kp.seed().decode()

profile = db.profile
user = {"dept_id":"",
		"dept_name":"",
		"dept_city":"",
		"dept_state":"",
		"dept_accno":publickey,
		"dept_secret":seed}
	

url = 'https://friendbot.stellar.org'
r = requests.get(url, params={'addr':publickey})      
print(publickey, seed)
curr_user_id = profile.insert_one(user).inserted_id


