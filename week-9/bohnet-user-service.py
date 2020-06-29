#
#============================================
# Title: Assignment 9.2
# Author: Chris Bohnet
# Date:23 JUne 2020
# Modified By: Chris Bohnet
# Description: Python program query and create documents in a MongoDB database instance through Python and pymongo
# Modifications: 
#============================================
#
from pymongo import MongoClient
import py
import pprint
import datetime

#connect to local
client=MongoClient('localhost', 27017)
db=client.web335

#create record
user= {
    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id" : "0000008",
    "date_created":datetime.datetime.utcnow()
}

#insert
user_id=db.users.insert_one(user).inserted_id

#display
print(user_id)
pprint.pprint(db.users.find_one({"employee_id":"0000008"}))
