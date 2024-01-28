import json

from miniblog.app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(db.Model, UserMixin):
    """ 用户数据库模型 """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Passage(db.Model):
    """ 文章数据库模型 """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True)
    create_time = db.Column(db.String(30))
    text = db.Column(db.Text(65536))

    def __init(self, title, create_time, text):
        self.title = title
        self.create_time = create_time
        self.text = text


class PersonalSetting:
    """ 个人设置数据库模型 """
    def __init__(self) -> None:
        file = open('personal.json', 'r')
        self.__data = json.load(file)
        file.close()
        self.__personal_setting = dict(self.__data)
    
    @property
    def get_webtitle(self):
        return self.__personal_setting['webtitle']
    
    @property
    def get_websignature(self):
        return self.__personal_setting['websignature']
    
    @property
    def get_nickname(self):
        return self.__personal_setting['nickname']
    
    @property
    def get_signature(self):
        return self.__personal_setting['signature']
    
    @property
    def get_statement(self):
        return self.__personal_setting['statement']
    
    @property
    def get_techweb(self):
        return self.__personal_setting['techweb']
    
    @property
    def get_otherweb(self):
        return self.__personal_setting['otherweb']
    
    @property
    def get_notedoc(self):
        return self.__personal_setting['notedoc']
    
    @property
    def get_codenote(self):
        return self.__personal_setting['codenote']
    
    @property
    def get_myproject(self):
        return self.__personal_setting['myproject']
    
    @property
    def get_recommandbook(self):
        return self.__personal_setting['recommandbook']
    
    def modify_webtitle(self, new_webtitle):
        self.__personal_setting['webtitle'] = new_webtitle
        self.__save()

    def modify_websignature(self, new_websignature):
        self.__personal_setting['websignature'] = new_websignature
        self.__save()

    def modify_nickname(self, new_nickname):
        self.__personal_setting['nickname'] = new_nickname
        self.__save()

    def modify_signature(self, new_signature):
        self.__personal_setting['signature'] = new_signature
        self.__save()

    def modify_statement(self, new_statement):
        self.__personal_setting['statement'] = new_statement
        self.__save()

    def append_techweb(self, title, url):
        self.__personal_setting['techweb'][title] = url
        self.__save()

    def append_otherweb(self, title, url):
        self.__personal_setting['otherweb'][title] = url
        self.__save()

    def append_notedoc(self, title, url):
        self.__personal_setting['notedoc'][title] = url
        self.__save()
    
    def append_codenote(self, title, url):
        self.__personal_setting['codenote'][title] = url
        self.__save()

    def append_myproject(self, title, url):
        self.__personal_setting['myproject'][title] = url
        self.__save()

    def append_recommandbook(self, title, url):
        self.__personal_setting['recommandbook'][title] = url
        self.__save()

    def __save(self):
        file = open('personal.json', 'w')
        json.dump(self.__personal_setting, file)
        file.close()
