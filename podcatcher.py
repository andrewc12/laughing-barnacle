#!/usr/bin/python3
import argparse
import yaml #python3-yaml
import sqlalchemy as sa #python3-sqlalchemy
from sqlalchemy.orm import sessionmaker
from table_def import Feed, Channel, Item
import requests
import xml.etree.ElementTree as ET #python3-elementtree


#set_defaults
cfg = {}
configfile = 'config.yml'

def save_config():
	with open(configfile, 'w') as ymlfile:
		yaml.dump(cfg, ymlfile)
	return

def load_config():
	global cfg
	with open(configfile, 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	return

def add_feed(url):
	# Create a feed
	new_feed = Feed(url)
	# Add the record to the session object
	session.add(new_feed)
	# commit the record the database
	session.commit()
	#result = requests.get(url)
	#c = result.content
	#root = ET.fromstring(c)
	#for child in root:
	#	print(child.tag, child.attrib)
	return



parser = argparse.ArgumentParser(description='TODO insert description')

parser.add_argument('--config', '-c')
parser.add_argument('--verbose',
	action='store_true',
	help='verbose flag' )
parser.add_argument('--importopml', '-i')
parser.add_argument('--exportopml', '-e')
parser.add_argument('--addfeed', '-a')
parser.add_argument('--deletefeed', '-d')

args = parser.parse_args()

#load the configuration file first so that the configuration can be overridden by flags
if args.config:
	configfile = args.config
try:
	load_config()
except FileNotFoundError as err:
	save_config()
	load_config()

#database connection
engine = sa.create_engine('sqlite:///podcasts.db', echo=True)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()













if args.addfeed:
	print("~ Add feed!")
	add_feed(args.addfeed)
else:
	print("~ Not add feed")




if args.verbose:
	print("~ Verbose!")
else:
	print("~ Not so verbose")


