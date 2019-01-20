from flask import Flask
import os
from pymongo import MongoClient
from bigchaindb_driver import BigchainDB

client = MongoClient('localhost', 27017)

app = None
db = None
bdb = None


def create_app():
    global db, app, bdb
    app = Flask(__name__)
    db = client.ihack
    bdb_root_url = 'https://test.bigchaindb.com/'
    bdb = BigchainDB(bdb_root_url)
    from app import views
    return app
