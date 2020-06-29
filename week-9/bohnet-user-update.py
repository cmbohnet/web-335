#
#============================================
# Title: Assignment 9.3
# Author: Chris Bohnet
# Date:23 JUne 2020
# Modified By: Chris Bohnet
# Description: Python program query and update documents in a MongoDB database instance through Python and pymongo
# Modifications: 
#============================================
#
from pymongo import MongoClient
import py
import pprint
import datetime

#connect to local instance
client=MongoClient('localhost', 27017)
db=client.web335

#db update
db.users.update_one= (
 { "employee_id" : "0000008"},
 {
     "$set":{
      "email": "cbohnet@my365.bellevue.edu"
     }
 } 
)

#find and output
pprint.pprint(db.users.find_one({"employee_id":"0000008"},
   {"email":1,"employee_id":1,"first_name":1,"last_name":1}))
