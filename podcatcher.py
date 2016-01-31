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
	return

def check_feed(feed):
	print("~ check_feed runs")
	print(feed.link)
	result = requests.get(feed.link)
	c = result.content
	root = ET.fromstring(c)
	for channeltag in root:
		#print(child.tag, child.attrib)
		if 'channel' in channeltag.tag:
			# editing Channel data
			try:
				feed, channel = session.query(Feed, Channel).filter(Feed.id==Channel.feed_id).first()
				channel.title = channeltag.find('title').text
				channel.link = channeltag.find('link').text
				channel.description = channeltag.find('description').text
				session.commit()
			except:
				feed.channels = [Channel(channeltag.find('title').text,channeltag.find('link').text,channeltag.find('description').text)]
				session.commit()
			for child in channeltag:
			#	print(child.tag, child.attrib, child.text)
				#case
				if 'item' in child.tag:
					for item in child:
						#print(item.tag, item.attrib, item.text)
						print(item.tag)
						if 'enclosure' in item.tag:
							print(item.tag, item.attrib['url'], item.text)
					try:
						channel, item = session.query(Channel, Item).filter(Channel.id==Item.channel_id).filter(Item.guid==child.find('guid').text).first()
						item.title = child.find('title').text
						item.link = child.find('link').text
						item.description = child.find('description').text
						item.author = child.find('author').text
						item.category = child.find('category').text
						item.comments = child.find('comments').text
						item.enclosure = child.find('enclosure').attrib['url']
						item.guid = child.find('guid').text
						item.pubDate = child.find('pubDate').text
						session.commit()
					except:
						more_items = [Item(child.find('title').text, child.find('link').text, child.find('description').text, child.find('author').text, child.find('category').text, child.find('comments').text, child.find('enclosure').attrib['url'], child.find('guid').text, child.find('pubDate').text)]
						print(more_items)
						channel.items.extend(more_items)
						session.commit()
					
						
				
	
	return

def check_feeds():
	print("~ check_feeds runs")
	# how to do a SELECT * (i.e. all)
	res = session.query(Feed).all()
	for feed in res:
		print (feed)
		check_feed(feed)
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
parser.add_argument('--updatefeeds', '-u', action='store_true')


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







if args.verbose:
	print("~ Verbose!")
else:
	print("~ Not so verbose")





if args.addfeed:
	print("~ Add feed!")
	add_feed(args.addfeed)

if args.updatefeeds:
	print("~ Update feeds!")
	check_feeds()



