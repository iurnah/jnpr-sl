#!/usr/bin/python

import pymongo
from pymongo import MongoClient 
import datetime

#db_name
#col_name

ask4db_name = 'Which Database? > '
ask4correct_db_name = 'Please enter a correct database: > '

ask4collection_name = 'Which collection? > '
ask4correct_col_name = 'Please enter a correct collection: > '

ask4newdb_name = 'Enter new database name: >'

'''check database already exist or not'''
def ck_db_exist(client, db_name):
	dbs = client.database_names()
	for db in dbs:
		if db == db_name:
			return True

	return False

'''check collection already exist or not'''
def ck_col_exist(client, db_name, col_name):
	db = client[db_name]
	cols = db.collection_names()
	for col in cols:
		if col == col_name:
			return True

	return False

'''show all Databases'''
def showDB(client):
	dbs = client.database_names()
	print 'the available databases are:\n'
	for db in dbs:
		print db 

'''show all collections'''
def showCol(client):
	#switch database
	db_name = raw_input(ask4db_name)
	while ck_db_exist(client, db_name) != True:
		global db_name
		db_name	= raw_input(ask4correct_db_name)

	db = client[db_name]
	cols = db.collection_names()
	for c in cols:
		print c 

	#switch collection		
	col_name = raw_input(ask4collection_name)
	while ck_col_exist(client, db_name, col_name) != True:
		global col_name
		col_name = raw_input(ask4correct_col_name)
		
	collections = db[col_name].find()
	for col in collections:
		print col

	print 'showCollection'


'''show all documents'''
def showDoc(client):
    	
	print 'showDoc'


'''Create Database'''
def createDB(client):
	newdb_name = raw_input(ask4newdb_name)
	newdb = client[newdb_name]
	newdb[newdb_name].insert({})

	print 'createDatabase'


'''Create API'''
def createDoc():
    print 'createDoc'

'''Read API'''
def readDoc():
    print 'readDoc'

'''update API'''
def updateDoc():
    print 'updateDoc'

'''delete API'''
def deleteDoc():
    print 'deleteDoc'

'''delete database'''
def deleteDB():
	print 'deletedb'

'''delete collection'''
def deleteCol():
    print 'deletecol'

#usage_prompt = 'This version support: \n\tshowdb, \n\tshowcol, \n\tshowdoc,\n\tnewdb, \n\tnewdoc, \n\treaddoc, \n\tupdatedoc, \n\tdeletedoc, \n\tdeletdb, \n\tdeletecol, \n\tquit \noperations!!'

usage_prompt = 'This version support: \n\tshowdb, \n\tshowcol, \n\tshowdoc,\n\tnewdb, \n\tquit' 

ask4host_prompt = 'Please enter host name: > '
ask4port_prompt = 'Please enter port number: > '

print usage_prompt
'''
connected = False
while not connected:
    #host = raw_input(ask4host_prompt)
    #port = raw_input(ask4port_prompt)

    client = MongoClient()
    #client1 = MongoClient('192.168.1.1', 27017)
    #client2 = MongoClient('localhost', 27017)
    connected = True

db = client.test_database
#print client
#print client1
#print client2
'''
client = MongoClient()

while True:
    cmd = raw_input('> ')   
    if cmd == 'showdb':
		showDB(client)
    elif cmd == 'showcol':
		showCol(client)
    elif cmd == 'showdoc':
		showDoc(client)
    elif cmd == 'newdb':
        createDB(client)
    elif cmd == 'newdoc':
		createDoc()
    elif cmd == 'readdoc':
		readDoc()
    elif cmd == 'updatedoc':
		updateDoc()
    elif cmd =='deletedoc':
		deleteDoc()
    elif cmd == 'deletedb':
        deleteDB()
    elif cmd == 'deletecol':
        deleteCol()
    elif cmd == 'quit':
		break
    else:
		print 'command not supported!!!\n'
		print usage_prompt

print 'Byebye!!!'
