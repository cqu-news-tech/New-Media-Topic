from flask import g
from flask_restful import Resource, reqparse
from common.models import PostAdvance, auth, db
from common.response import Resp
from datetime import datetime

post_data = reqparse.RequestParser()
post_data.add_argument('post_id', type=int)
post_data.add_argument('uid', type=int)
post_data.add_argument('plan_id', type=int)
post_data.add_argument('director', type=str)
post_data.add_argument('finish_time', type=str)
post_data.add_argument('read_num', type=int)
post_data.add_argument('content', type=str)

class AdvancePost(Resource):
    @auth.login_required
    def post(self):
        post_json = post_data.parse_args()
        if post_json['post_id']:
            post_advance = PostAdvance.query.get(post_json['post_id'])
            post_advance.plan_id = post_json['plan_id']
            post_advance.create_time = datetime.now()
            post_advance.director = post_json['director']
            post_advance.finish_time = post_json['finish_time']
            post_advance.read_num = post_json['read_num']
            post_advance.content = post_json['content']
        else:
            post_advance = PostAdvance()
            post_advance.uid = post_json['uid']
            post_advance.plan_id = post_json['plan_id']
            post_advance.create_time = datetime.now()
            post_advance.director = post_json['director']
            post_advance.finish_time = post_json['finish_time']
            post_advance.read_num = post_json['read_num']
            post_advance.content = post_json['content']

        db.session.add(post_advance)
        db.session.commit()
        return Resp(msg='提交成功').json
