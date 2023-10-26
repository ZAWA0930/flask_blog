

from flask_migrate import Migrate
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager




app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
uri=os.environ.get('DATABASE_URL')

if uri:
    if uri.startswith('postgres://'):
        uri=uri.replace('postgres://', 'postgresql://',1)
        app.config['SQLALCHEMY_DATABASE_URI']=uri

else:
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Taichi4649@localhost'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

def localize_callback(*args, **kwargs):
    return 'このページにアクセスするには、ログインが必要です。'
login_manager.localize_callback = localize_callback

###SQLITE外部キー制約
# from sqlalchemy.engine import Engine
# from sqlalchemy import event

# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     cursor = dbapi_connection.cursor()
#     cursor.execute("PRAGMA foreign_keys=ON")
#     cursor.close()



from blog.main.views import main
from blog.users.views import users
from blog.error_pages.handlers import error_pages

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(error_pages)