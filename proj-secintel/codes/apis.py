#!/usr/bin/python

import pymongo
from pymongo import MongoClient
import datetime

#print the simple prompt when program start up
usage_prompt0 = '****************************************'
usage_prompt1 = 'API write inpymongo for spotlight test bed\n'
usage_prompt2 = 'This version support: \n\tshowdbs,\n\tnewdb,\n\treaddb,\n\tquit'
print usage_prompt0
print usage_prompt1
print usage_prompt2

#show exist database
#TODO: add more info about Databases
def showDBs(connectoin):
	dbs = connection.database_names()
	print 'we have databases: '
	for db in dbs:
		print '\t' + db

#create a new "database", in fact of a "collection" in MongoDB
def newDB(connection, ui_db_name, ui_category):
	mongo_db_name = ui_db_name + ui_category
	newdb = connection[mongo_db_name]
	newdb[mongo_db_name].insert({})
	print 'New database \"%s\" has been created' % (mongo_db_name)

#insert()
#read a database content, collection.find()
#TODO: add queryCriteria, maybe multiple of them:
def readDB(connection, ui_db_name, ui_category, queryCriteria):
	mongo_db_name = ui_db_name + ui_category
	mongo_db = connection[mongo_db_name]
	documents = mongo_db[mongo_db_name].find()
	print 'collection \"%s\" have following docs:\n'
	for doc in documents:
		print doc
	print '\nRead \"%s\" done! ' % (mongo_db_name)

#update database
def updateDB(connection, ui_db_name, ui_category, queryCriteria, newValue):
	#call readDB() before updateDB()
	print 'In update!'
	
#delete database
def delete(connection, ui_db_name, ui_category, queryCriteria):
	print "In delete!"

#connect to the MongoDB server
try:
	connection = MongoClient()
except:
	print("Error: Unable to connect to database.")
	connection = None

#main function
while True:
	cmd = raw_input('> ')
	if 	cmd == 'showdbs':
		showDBs(connection)
	elif cmd == 'newdb':
		ui_db_name = raw_input('Enter Database Name:> ')
		ui_category = raw_input('Enter Category Name:> ')
		newDB(connection, ui_db_name, ui_category)
 	elif cmd == 'readdb':
		ui_db_name = raw_input('Enter Database Name:> ')
		ui_category = raw_input('Enter Category Name:> ')
		readDB(connection, ui_db_name, ui_category, queryCriteria) 
	elif cmd == 'update':
		ui_db_name = raw_input('Enter Database Name:> ')
		ui_category = raw_input('Enter Category Name:> ') 
		updateDB(connection, ui_db_name, ui_category, queryCriteria, newValue)
	elif cmd == 'delete':
		ui_db_name = raw_input('Enter Database Name:> ')
		ui_category = raw_input('Enter Category Name:> ')
		delete(connection, ui_db_name, ui_category, queryCriteria)
	elif cmd == 'quit':
		break
	else:
		print 'command not supported!!\n'
		print usage_prompt2

print '\nByeby!!\n'
