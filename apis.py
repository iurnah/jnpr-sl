#!/usr/bin/python

import pymongo
from pymongo import MongoClient
import datetime

#print the simple prompt when program start up
usage_prompt0 = '****************************************'
usage_prompt1 = 'API write inpymongo for spotlight test bed\n'
usage_prompt2 = 'This version support: \n\tnewdb,\n\tshowdb,\n\tquit'
print usage_prompt0
print usage_prompt1
print usage_prompt2

#create a new database
def newDB(client, db_name):
	print 'newdb has been created'	 

#connect to the MongoDB server
try:
	connection = MongoClient()
except:
	print("Error: Unable to connect to database.")
	connection = None

#main function
while True:
	cmd = raw_input('> ')
	if cmd == 'newdb':
		db_name = raw_input('Enter Database Name:> ')
		newDB(connection, db_name)
	elif cmd == 'showdb':
		db_name = raw_input('Enter Database Name:> ')
		showDB(connection, db_name)
	elif cmd == 'showcol':
		db_name = raw_input('Enter Database Name:> ')
		col_name = raw_input('Enter Database Name:> ')
		showCol(connection, db_name, col_name)
	elif cmd == 'quit':
		break
	else:
		print 'command not supported!!\n'
		print usage_prompt2

print '\nByeby!!\n'


