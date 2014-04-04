#coding=utf-8
from sqlalchemy import Column, Integer, String, Text
from database import Base, db_session
from datetime import datetime

class News(Base):
	__tablename__ = 'news'
	id = Column(Integer,primary_key=True)
	title = Column(String(120), nullable=False)
	image = Column(String(200))
	author = Column(String(20))
	time = Column(String(20))
	source = Column(String(20))
	category = Column(String(80))
	abstract = Column(Text)
	content = Column(Text)
	
	def __init__(self, title="", abstract="", content="", image="",\
	 author="", time="", source="", category=""):
		self.title = title
		self.abstract = abstract
		self.content = content
		self.image = image
		self.author = author
		self.time = time
		self.source = source
		self.category = category

	def __repr__(self):
		return '<News %r>' %self.title #return the object