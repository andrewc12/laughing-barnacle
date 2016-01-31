#!/usr/bin/python3
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

engine = sa.create_engine('sqlite:///podcasts.db', echo=True)
Base = declarative_base()

########################################################################
class Feed(Base):
	""""""
	__tablename__ = "feeds"
	
	id = sa.Column(sa.Integer, primary_key=True)
	link = sa.Column(sa.String, nullable=False)
	
	#----------------------------------------------------------------------
	def __init__(self, link):
		""""""
		self.link = link

########################################################################
class Channel(Base):
	""""""
	__tablename__ = "channels"
	
	id = sa.Column(sa.Integer, primary_key=True)
	title = sa.Column(sa.String, nullable=False)
	link = sa.Column(sa.String, nullable=False)
	description = sa.Column(sa.String, nullable=False)
	
	feed_id = sa.Column(sa.Integer, sa.ForeignKey("feeds.id"))
	feed = sa.orm.relationship("Feed", backref=sa.orm.backref("channels", order_by=id))
	
	#----------------------------------------------------------------------
	def __init__(self, title, link, description):
		""""""
		self.title = title
		self.link = link
		self.description = description
		
########################################################################
class Item(Base):
	""""""
	__tablename__ = "items"
	
	id = sa.Column(sa.Integer, primary_key=True)
	title = sa.Column(sa.String, nullable=False)
	link = sa.Column(sa.String, nullable=False)
	description = sa.Column(sa.String, nullable=False)
	author = sa.Column(sa.String, nullable=False)
	category = sa.Column(sa.String, nullable=False)
	comments = sa.Column(sa.String, nullable=False)
	enclosure = sa.Column(sa.String, nullable=False)
	guid = sa.Column(sa.String, nullable=False)
	pubDate = sa.Column(sa.String, nullable=False)
	
	channel_id = sa.Column(sa.Integer, sa.ForeignKey("channels.id"))
	channel = sa.orm.relationship("Channel", backref=sa.orm.backref("items", order_by=id))
	
	#----------------------------------------------------------------------
	def __init__(self, title, link, description, author, category, comments, enclosure, guid, pubDate):
		""""""
		self.title = title
		self.link = link
		self.description = description
		self.author = author
		self.category = category
		self.comments = comments
		self.enclosure = enclosure
		self.guid = guid
		self.pubDate = pubDate
		
# create tables
Base.metadata.create_all(engine)
