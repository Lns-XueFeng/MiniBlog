import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4
from flask_ckeditor import CKEditor
from flask_frozen import Freezer

from miniblog.config import config


miniblog_absdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(config["development"])

login_manager = LoginManager(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)
ckeditor = CKEditor(app)


@login_manager.user_loader
def user_loader(user_id):
    user = Admin.query.get(int(user_id))
    return user


@app.template_global()
def get_length(dic):
    return len(dic)


from miniblog.command import *
from miniblog.blog import *
from miniblog.admin import *


if __name__ == '__main__':
    app.run(user_loader=True, debug=True)
