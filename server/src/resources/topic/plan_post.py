from flask import g
from flask_restful import Resource, reqparse
from common.models import PostPlan, auth, db
from common.response import Resp
from datetime import datetime

post_data = reqparse.RequestParser()
post_data.add_argument('post_id', type=int)
post_data.add_argument('title', type=str)
post_data.add_argument('content', type=str)
post_data.add_argument('state', type=int)

class PLanPost(Resource):
    @auth.login_required
    def post(self):
        post_json = post_data.parse_args()
        if post_json['post_id']:
            post_plan = PostPlan.query.filter_by(id = post_json['post_id']).first()
            post_plan.create_time = datetime.now()
            post_plan.title = post_json['title']
            post_plan.content = post_json['content']
            post_plan.state = post_json['state']
        else:
            post_plan = PostPlan()
            post_plan.uid = g.user.id
            post_plan.create_time = datetime.now()
            post_plan.title = post_json['title']
            post_plan.content = post_json['content']

        db.session.add(post_plan)
        db.session.commit()
        return Resp(msg='提交成功').json
