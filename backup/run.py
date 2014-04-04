#coding=utf-8
from flask import Flask, request, session, g, redirect, url_for, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin
from flask.ext.admin.contrib import sqlamodel
from wtforms import fields, widgets
import os.path as op
from database import db_session #数据库session, 用于操作数据库，如db_session.add(u), db_session.commit()
from projects import Project
from news import News
import hashlib
import sys
import os
import Image
from werkzeug import secure_filename
#from database import init_db
#init_db()

# configuration
DEBUG = True
SECRET_KEY = 'sparkmorry'

UPLOAD_FOLDER="static/files/"
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')
 # Define wtforms widget and field

class CKTextAreaWidget(widgets.TextArea):
	def __call__(self, field, **kwargs):
		kwargs.setdefault('class_', 'ckeditor')
		return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
	widget = CKTextAreaWidget()

class Test(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.UnicodeText)

class TestAdmin(sqlamodel.ModelView):
	form_overrides = dict(text=CKTextAreaField)
	create_template = 'edit.html'
	edit_template = 'edit.html'

admin = Admin(app)
admin.add_view(ModelView(Project, db_session))
admin.add_view(ModelView(News, db_session))
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/intro')
def intro():
	return render_template('intro.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method=='POST':
		print 'submit'

		for project in Project.query.all(): #查询所有Project对象里是否有该公司
				if request.form['company'] == project.company:
					session['error']='该公司项目已经被注册'
					error = session['error']				
					return render_template('register.html', error = error)
		'''
		if request.files['file_path']:
			upload_picture = request.files['file_path']
			file_name = upload_picture.filename #获取图片文件名称	
			print file_name
			file_path = UPLOAD_FOLDER+file_name
		'''

		newcompany=Project(request.form['company'], request.form['address'],request.form['invest'],\
			request.form['time'],request.form['name'],request.form['major'],\
			request.form['phone'],request.form['email'],request.form['position'],\
			request.form['holds'],request.form['introduction'],request.form['team'],\
			request.form['business'],request.form['file_path'])
		db_session.add(newcompany) #执行数据库操作
		db_session.commit()

	return render_template('register.html')

@app.route('/judges')
def judges():
	return render_template('judges.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/notification')
def notification():
	return render_template('notification.html')


if __name__ == '__main__':
    app.run()
