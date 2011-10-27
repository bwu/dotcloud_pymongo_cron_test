#!/usr/bin/env python

import json
import facebook

from datetime import datetime
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

# Give todays date as an item in a dictionary.
today = { 'date and time' : datetime.today() }
collection.insert(today)
