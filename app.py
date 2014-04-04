#coding=utf-8
from flask import Flask
from flask_peewee.db import Database

# create our little application :)
app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)