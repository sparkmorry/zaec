from app import app, db

from auth import *
from admin import admin
from models import *
from views import *

admin.setup()

if __name__ == '__main__':
	Photo.create_table(fail_silently=True)
	Project.create_table(fail_silently=True)
	News.create_table(fail_silently=True)
	app.run()