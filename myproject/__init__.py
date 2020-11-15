import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,current_user
from flask_restful import Api


app = Flask(__name__)

active_users = []

# თუ კონფიგურაციისათვის იყენებთ ბევრ პარამეტრს სასურველია მათი config.py ფაილში გადანაწილება 
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()
Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from myproject.auth.views import auth_blueprint
from myproject.navbar.views import navbar_blueprint
from myproject.index.views import index_blueprint
from myproject.profile.views import profile_blueprint
from myproject.admin.views import admin_blueprint
from myproject.post.views import post_blueprint

from myproject.models import Post

app.register_blueprint(auth_blueprint,url_prefix="/")
app.register_blueprint(navbar_blueprint,url_prefix="/")
app.register_blueprint(index_blueprint,url_prefix="/")
app.register_blueprint(profile_blueprint,url_prefix="/")
app.register_blueprint(admin_blueprint,url_prefix="/")
app.register_blueprint(post_blueprint,url_prefix="/")


from myproject.resources.PostsApi import PostsApi
api = Api(app)
api.add_resource(PostsApi,'/getPosts')