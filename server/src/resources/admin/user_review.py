from flask_restful import Resource, reqparse
from common.models import User, auth, admin_required, db
from common.response import Resp


post_data = reqparse.RequestParser()
post_data.add_argument('uid', type=int)


class UserReview(Resource):
    @auth.login_required
    @admin_required
    def get(self):
        user_review_list = User.query.filter_by(is_verify = False).all()
        data = []
        for item in user_review_list:
            data.append(item.json)
        return Resp({"list": data}).json

    @auth.login_required
    @admin_required
    def post(self):
        post_json = post_data.parse_args()
        user = User.query.get(post_json['uid'])
        user.is_verify = True
        db.session.add(user)
        db.session.commit()
        return Resp(msg='用户身份审核成功').json