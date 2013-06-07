#!/usr/bin/python

import pymongo
from pymongo import MongoClient
import datetime

usage_prompt = 'This version support: \n\tcreatedb,\n\tshowdb,\n\tquit'

client = MongoClient()

while True:
	cmd = raw_input('> ')
	if cmd == 'createdb':
		db_name = rawinput('Enter Database Name:> ')
		newDB(client, db_name)
	elif cmd == 'showdb':
		db_name = rawinput('Enter Database Name:> ')
		showDB(client, db_name)
	elif cmd == 'showcol':
		db_name = rawinput('Enter Database Name:> ')
		col_name = rawinput('Enter Database Name:> ')
		showCol(client, db_name, col_name)
	elif cmd == 'quit':
		break
	else:
		print 'command not supported!!\n'
		print usage_prompt

print '\nByeby!!\n'


