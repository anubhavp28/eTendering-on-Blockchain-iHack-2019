from flask import Flask
import os
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

app = None
db = None

def create_app():
    global db, app
    app = Flask(__name__)
    
    db = client.ihack
    
    from app import views
    return app
