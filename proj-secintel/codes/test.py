#!/usr/bin/python

import pymongo
import datetime

from pymongo import MongoClient
#connect to mongodb server
client = MongoClient()

print client.database_names()
#get database, db is defined take the test data base from mongodb 
#db = client.local
db = client.test
#dbs = db.show()
#print db.name()

#get collection
#collection = db.test

#document post
post = {"author": "Mike",
		"text": "My first blog post!",
		"tags": ["mongodb", "python", "pymongo"],
		"date": datetime.datetime.utcnow()}

#new collection called posts
posts = db.posts
post_id = posts.insert(post)
print post_id

all_collection = db.collection_names()
print all_collection  	 


all_docs = db.posts.find()
print all_docs

'''
myCursor = collection.find({'a': 1})

myDoc = myCursor.hasNext() 
#? myCursor.next() : null

print myDoc

print myCursor

collection.find({'autr': ''})

print collection.find({'author': 'rui'})
'''

print "\nWorked!!!\n"

