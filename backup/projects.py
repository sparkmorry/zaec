#coding=utf-8
from sqlalchemy import Column, Integer, String
from database import Base, db_session

class Project(Base):
	__tablename__ = 'projects'
	id = Column(Integer,primary_key=True)
	company = Column(String(120), nullable=False)
	address = Column(String(80))
	invest = Column(String(20))
	time = Column(String(20))
	name = Column(String(20))
	major = Column(String(20))
	phone = Column(String(20))
	email = Column(String(80))
	position = Column(String(20))
	holds = Column(String(20))
	introduction = Column(String(300))
	team = Column(String(300))
	business = Column(String(300))
	file_path = Column(String(200))
	
	def __init__(self, company="", address="", invest="", time="", name="",\
	 major="", phone="", email="", position="", holds="", introduction="", \
	 team="", business="", file_path=""):
		self.company = company
		self.address = address
		self.invest = invest
		self.time = time
		self.name = name
		self.major = major
		self.phone = phone
		self.email = email
		self.position = position
		self.holds = holds
		self.introduction = introduction
		self.team = team
		self.business = business
		self.file_path = file_path

	def __repr__(self):
		return '<Project %r>' %self.company #return the object