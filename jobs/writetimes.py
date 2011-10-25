#!/usr/bin/env python

import json
import csv

from pymongo import Connection

# Open the environment file and get the name of the host and port
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

# Assign the host and port
host = env['DOTCLOUD_DATA_MONGODB_URL']

# Connect to the database and assign the correct name for the database and collection
connection = Connection(host=host)
db = connection.tests
collection = db.times

# Create the row writer and write the first row
FILE_NAME = 'times.csv'
rowWriter = csv.writer(open(FILE_NAME, 'wt'), delimiter = ",")
firstrow = ['Word', 'Actual Date and Time']
rowWriter.writerow(firstrow)

# Writes all subsequent rows
for time in collection.find():
	row = []
	row.append('Word up!')
	row.append(time['date and time'])
	rowWriter.writerow(row)