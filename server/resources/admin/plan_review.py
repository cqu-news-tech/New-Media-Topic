from flask_restful import Resource, reqparse
from common.models import PostPlan, auth, admin_required, db
from common.response import Resp

post_data = reqparse.RequestParser()
post_data.add_argument('post_id', type=int)
post_data.add_argument('state', type=int)

class PlanReview(Resource):
    @auth.login_required
    @admin_required
    def post(self):
        post_json = post_data.parse_args()
        post_review = PostPlan.query.get(post_json['post_id'])
        post_review.state = post_json['state']
        db.session.add(post_review)
        db.session.commit()
        return Resp(msg='提交成功').json