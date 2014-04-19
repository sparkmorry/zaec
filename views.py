#coding=utf-8
from flask import request, redirect, url_for, render_template, flash

from flask_peewee.utils import get_object_or_404, object_list
from werkzeug import secure_filename
import os

from app import app
from auth import auth
from models import Photo, Note, Project, News

'''
	包括页面：
	1. 管理员页面:
	   add.html 新增新闻/活动等编辑页面
	   edit.html 修改新闻/活动等编辑页面

	2. 网站首页入口页面：
	   url 				页面 				说明
	   -------------------------------------------------
	   / 				index.html 			首页
	   /intro 			intro.html 			大赛介绍页面
	   /notification 	notification.html 	活动公告页面（暂定均显示最新6个）
	   /judges 			judges.html 		评委顾问页面
	   /projects 		projects.html 		项目展示页面（暂定显示最新10个）
	   往届回顾								直接连接到上届网站首页
	   /register		register.html 		我要参赛页面

	3. 文章页面：
	   url 				页面 				说明
	   -------------------------------------------------
	   /events 			e_list.html 		查看更多后的活动列表标题页面
	   /news 			n_list.html 		查看更多后的活动列表标题页面
	   /projects 		p_list.html 		查看更多后的项目列表标题页面
	   /news/id 		news.html 			新闻文章页面
	   /event/id 		event.html 			活动文章页面
	   /project/id 		project.html 		项目文章页面
'''
#首页
@app.route('/')
def index():
	notifications = News.select().where(
		News.category == 'NOTIFICATION'
		).order_by(News.time.desc()).limit(5)
	news = News.select().where(
		News.category == 'NEWS'
		).order_by(News.time.desc()).limit(6)
	pics = News.select().where(
		News.category == 'PICTURE'
	)
	pic_num = pics.count()
	#通知与公告 notification 热门新闻 news
	return render_template('index.html', 
		notification_list = notifications, 
		news_list = news, pics=pics, pic_num=pic_num)

#大赛介绍页面
@app.route('/intro')
def intro():
	return render_template('intros/intro.html')

@app.route('/intro/1')
def intro1():
	return render_template('intros/intro1.html')

@app.route('/intro/2')
def intro2():
	return render_template('intros/intro2.html')

@app.route('/intro/3')
def intro3():
	return render_template('intros/intro3.html')

@app.route('/intro/4')
def intro4():
	return render_template('intros/intro4.html')

#我要参赛页面
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

#评委顾问页面
@app.route('/judges')
def judges():
	return render_template('judges.html')

#新闻文章页面
@app.route('/news/<news_id>')
def news(news_id):
	news = News.select().where(
		News.id == news_id 
		).get()

	#news_list
	news_list = News.select().where(
		News.category == 'NEWS'
	).order_by(News.time.desc()).limit(10)

	#最新的10个新闻news_list 及指定的新闻文章news
	return render_template('articles/news.html', 
		news = news, news_list = news_list)

#所有新闻列表标题页面（显示更多）
@app.route('/news')
def news_list():
	#news_list
	news_list = News.select().where(
		News.category == 'NEWS'
	).order_by(News.time.desc()).limit(20)

	return render_template('articles/n_list.html', news_list = news_list)

#所有活动列表标题页面（显示更多）
@app.route('/events')
def events_list():
	#news_list
	news_list = News.select().where(
		News.category == 'ACTIVITY'
	).order_by(News.time.desc()).limit(20)
	return render_template('articles/e_list.html', events_list = news_list)

#活动文章页面
@app.route('/event/<news_id>')
def events(news_id):
	news = News.select().where(
		News.id == news_id 
		).get()

	#news_list
	news_list = News.select().where(
		News.category == 'ACTIVITY'
	).order_by(News.time.desc()).limit(10)
	#print news.title
	return render_template('articles/events.html', 
		news = news, events_list = news_list)

#项目展示最新10个
@app.route('/projects')
def projects():
	news =  News.select().where(
		News.category == 'PROJECT'
	).order_by(News.time.desc()).limit(10)
	return render_template('projects.html', project_list = news)

@app.route('/project/<news_id>')
def project(news_id):
	news =  News.select().where(
		News.category == 'PROJECT'
	).order_by(News.time.desc()).limit(10)

	project = News.select().where(
		News.id == news_id 
		).get()
	return render_template('articles/project.html', news=project, project_list = news)

#活动公告页面
@app.route('/notification')
def notification():
	news = News.select().where(
		News.category == 'NEWS'
		).order_by(News.time.desc()).limit(6)

	events = News.select().where(
		News.category == 'ACTIVITY'
		).order_by(News.time.desc()).limit(6)

	#展示最新的6个新闻摘要news_list和活动摘要events_list
	return render_template('notification.html',
		news_list = news, events_list = events)

