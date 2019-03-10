from flask import g
from flask_restful import Resource, reqparse
from common.models import PostPlan, PostAdvance, auth
from common.response import Resp


post_data = reqparse.RequestParser()
post_data.add_argument('post_id', type=int)
post_data.add_argument('uid', type=int)


class PlanDetail(Resource):
    @auth.login_required
    def post(self):
        post_json = post_data.parse_args()
        post_plan = getattr(
            PostPlan.query.get(post_json['post_id']),
            'json',
            {}
        )
        post_advance = getattr(
            PostAdvance.query.filter_by(plan_id = post_json['post_id']).first(),
            'json',
            {}
        )
        if post_json['uid'] == g.user.id:
            can_edit = True
        else:
            can_edit = False
        data = {
            "can_edit": can_edit or g.user.is_admin,
            "plan": post_plan,
            "advance": post_advance
        }
        return Resp(data, msg='获取选题详情成功').json
