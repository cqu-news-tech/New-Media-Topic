from flask import g
from flask_restful import Resource, reqparse
from common.models import auth, db
from common.response import Resp

post_data = reqparse.RequestParser()
post_data.add_argument('name', type=str)
post_data.add_argument('phone', type=int)

class Profile(Resource):
    @auth.login_required
    def get(self):
        data = {
            'name': g.user.name,
            'phone': g.user.phone
        }
        return Resp(data, msg='获取资料成功').json

    @auth.login_required
    def post(self):
        post_args = post_data.parse_args()
        g.user.name = post_args['name']
        g.user.phone = post_args['phone']
        db.session.add(g.user)
        db.session.commit()
        return Resp(msg='更新资料成功').json