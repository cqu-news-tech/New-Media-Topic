from functools import wraps
from flask import Flask, g
from flask_restful import Api
from common.response import Resp
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from flask_wxapp import WXApp
import config

# initialization
app = Flask(__name__)
app.config.from_object(config)

# extensions
wxapp = WXApp()
wxapp.init_app(app)
db = SQLAlchemy(app)
api = Api(app)
auth = HTTPTokenAuth(scheme='Bearer')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(32), index=True)
    unionid = db.Column(db.String(32), index=True)
    name = db.Column(db.String(32))
    phone = db.Column(db.BigInteger)
    is_verify = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)


    @property
    def is_register(self):
        if self.name and self.phone:
            return True
        else:
            return False
    @property
    def token(self, expiration=7200):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return 'Bearer ' + s.dumps({'id': self.id}).decode('ascii')

    @property
    def json(self):
        return {
            'name': self.name,
            'uid': self.id,
            'phone': self.phone
        }


class PostPlan(db.Model):
    __tablename__ = 'post_plan'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True)
    create_time = db.Column(db.DateTime)
    state = db.Column(db.Integer, index=True, default=1)
    is_expired = db.Column(db.Boolean, default=False)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)


    @property
    def json(self):
        return {
            "uid": self.uid,
            "post_id": self.id,
            "create_time": self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            "state": self.state,
            "title": self.title,
            "content": self.content,
            "is_expired": self.is_expired
        }


class PostAdvance(db.Model):
    __tablename__ = 'post_advance'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True)
    plan_id = db.Column(db.Integer, index=True)
    create_time = db.Column(db.DateTime)
    state = db.Column(db.Integer, index=True, default=1)
    is_expired = db.Column(db.Boolean, default=False)
    director = db.Column(db.String(32))
    finish_time = db.Column(db.Date)
    read_num = db.Column(db.Integer)
    content = db.Column(db.Text)

    @property
    def json(self):
        return {
            "post_id": self.id,
            "plan_id": self.plan_id,
            "create_time": self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            "state": self.state,
            "director": self.director,
            "finish_time": self.finish_time.strftime('%Y-%m-%d'),
            "read_num": self.read_num,
            "content": self.content
        }


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True)
    create_time = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, index=True)
    post_type = db.Column(db.String(16))
    content = db.Column(db.Text)


@auth.verify_token
def verify_auth_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return False  # valid token, but expired
    except BadSignature:
        return False  # invalid token
    g.user = User.query.get(data['id'])
    return True


@auth.error_handler
def unauthorized():
    return Resp(status=10401).json

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if g.user.is_admin:
            return func(*args, **kwargs)
        else:
            return Resp(status=10403).json
    return wrapper