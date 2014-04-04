# config

class Configuration(object):
	DATABASE = {
		'name': 'zaec',
		'engine': 'peewee.MySQLDatabase',
		'user': 'root',
		'passwd': '',
	}

	DEBUG = True
	SECRET_KEY = 'shhhh'
	IMAGE_FOLDER = 'static/upload_image'
	IMAGE_URL = '/static/upload_image/'
	PROJECT_FOLDER = 'static/projects'