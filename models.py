#coding=utf-8
# models.py
import datetime
import os

from flask import Markup
from peewee import *
from werkzeug import secure_filename

from app import app, db
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Photo(db.Model):
    image = CharField()

    def __unicode__(self):
        return self.image

    def save_image(self, file_obj):
        self.image = file_obj.filename
        full_path = os.path.join(app.config['IMAGE_FOLDER'], self.image)
        file_obj.save(full_path)
        self.save()

    def url(self):
        return os.path.join(app.config['IMAGE_URL'], self.image)

    def thumb(self):
        return Markup('<img src="%s" style="height: 80px;" />' % self.url())


class Note(db.Model):
    message = TextField()
    created = DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return '%s: %s' % (self.message, self.created)

class Project(db.Model):
    company = CharField()
    address = CharField()
    invest = CharField()
    time = CharField()
    name = CharField()
    major = CharField()
    phone = CharField()
    email = CharField()
    position = CharField()
    holds = CharField()
    introduction = TextField()
    team = TextField()
    business = TextField()
    file_path = TextField()

    def __unicode__(self):
        return '%s: %s' % (self.company, self.phone)

class News(db.Model):
    title = CharField()
    image = CharField(null = False, default='')
    author = CharField(null = False, default='')
    time = DateTimeField(default=datetime.datetime.now)
    source = CharField(null = False, default='')
    abstract = TextField(default='')
    content = TextField(default='')
    category = CharField(choices=[('NEWS', '新闻'),
                                  ('ACTIVITY', '活动'),
                                  ('PEOPLE', '评委'),
                                  ('PICTURE', '轮播图片'),
                                  ('PROJECT', '项目展示'),
                                  ('NOTIFICATION', '通告')
                                  ])
    def __unicode__(self):
        return '%s: %s %s' % (self.title, self.author, self.category)        