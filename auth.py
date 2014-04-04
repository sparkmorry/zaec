from flask_peewee.auth import Auth

from app import app, db

auth = Auth(app, db)
auth.User.create_table(fail_silently=True)  # make sure table created.
admin = auth.User(username='admin', email='', admin=True, active=True)
admin.set_password('123456')
#admin.save()