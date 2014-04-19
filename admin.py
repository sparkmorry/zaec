# admin.py
import datetime
from flask import request
from flask_peewee.db import Database
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin, ModelAdmin
from wtforms.fields import FileField, HiddenField
from wtforms.form import Form

from app import app, db
from auth import auth
from models import Photo, Note, Project, News

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

admin = Admin(app, auth)

class PhotoAdmin(ModelAdmin):
    columns = ['image', 'thumb']

    def get_form(self, adding=False):
        class PhotoForm(Form):
            image = HiddenField()
            image_file = FileField(u'Image file')

        return PhotoForm

    def save_model(self, instance, form, adding=False):
        instance = super(PhotoAdmin, self).save_model(instance, form, adding)
        if 'image_file' in request.files:
            file = request.files['image_file']
            instance.save_image(file)
        return instance
'''
class NoteAdmin(ModelAdmin):
	columns = ('message','created')

	def get_template_overrides(self):
		return {'edit': 'edit.html'}	
'''

class ProjectAdmin(ModelAdmin):
    columns = ('company','phone')

class NewsAdmin(ModelAdmin):
    columns = ('title','author','category')
    
    def get_template_overrides(self):
        return {'edit': 'admin/edit.html',
        'add': 'admin/add.html'}  

#admin.register(Note, NoteAdmin)
admin.register(Photo, PhotoAdmin)
admin.register(Project, ProjectAdmin)
admin.register(News, NewsAdmin)