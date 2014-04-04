#coding=utf-8
from flask import request, redirect, url_for, render_template, flash

from flask_peewee.utils import get_object_or_404, object_list
from werkzeug import secure_filename
import os

from app import app
from auth import auth
from models import Photo, Note, Project, News


@app.route('/')
def index():
	notifications = News.select().where(
		News.category == 'NOTIFICATION'
		).order_by(News.time.desc()).limit(5)
	news = News.select().where(
		News.category == 'NEWS'
		).order_by(News.time.desc()).limit(6)
	return render_template('index.html', 
		notification_list = notifications,
		news_list = news)

@app.route('/intro')
def intro():
	return render_template('intro.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	
	if request.method=='POST' and request.form['company']:

		#deal with uploaded files
		full_path = ''
		if request.files['file_path']:
			file_obj = request.files['file_path']
			file_name = file_obj.filename
			full_path = os.path.join(app.config['PROJECT_FOLDER'], file_name)
			file_obj.save(full_path)

		#insert a new project
		project = Project(company = request.form['company'],
			address = request.form['address'],
			invest = request.form['invest'],
			time = request.form['time'],
			name = request.form['name'],
			major = request.form['major'],
			phone = request.form['phone'],
			email = request.form['email'],
			position = request.form['position'],
			holds = request.form['holds'],
			introduction = request.form['introduction'],
			team = request.form['team'],
			business = request.form['business'],
			file_path = full_path
		)
		project.save()
		msg = 'success'

		return render_template('register.html', msg = msg)
	print 'not'
	return render_template('register.html')

@app.route('/judges')
def judges():
	return render_template('judges.html')

@app.route('/news/<news_id>')
def news(news_id):
	news = News.select().where(
		News.id == news_id 
		).get()

	#news_list
	news_list = News.select().where(
		News.category == 'NEWS'
	).order_by(News.time.desc()).limit(10)
	print news.title
	return render_template('news.html', 
		news = news, news_list = news_list)

@app.route('/projects')
def projects():
	news =  News.select().where(
		News.category == 'PROJECT'
	).order_by(News.time.desc()).limit(10)
	return render_template('projects.html', project_list = news)

@app.route('/notification')
def notification():
	news = News.select().where(
		News.category == 'NEWS'
		).order_by(News.time.desc()).limit(6)
	return render_template('notification.html',
		news_list = news)

