from flask import g
from flask_restful import Resource, reqparse
from common.models import PostPlan, auth, db
from common.response import Resp

post_data = reqparse.RequestParser()
post_data.add_argument('post_id')

class MyTopic(Resource):
    @auth.login_required
    def get(self):
        user_id = g.user.id
        plan_list = PostPlan.query.filter_by(uid = user_id).all()
        temp = []
        for item in plan_list:
            temp.append(item.json)
        return Resp({
            'list': temp
        }).json

    @auth.login_required
    def post(self):
        post_id = post_data.parse_args()['post_id']
        post_plan = PostPlan.query.get(post_id)
        post_plan.is_expired = not post_plan.is_expired
        db.session.add(post_plan)
        db.session.commit()
        return Resp(msg='选题状态已改变').json


