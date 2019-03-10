from flask import g
from flask_restful import Resource, reqparse
from common.models import Comments, admin_required, auth, db
from common.response import Resp
from datetime import datetime


post_data = reqparse.RequestParser()
post_data.add_argument('post_id', type=int)
post_data.add_argument('post_type', type=str)
post_data.add_argument('content', type=str)


class CommentsPost(Resource):
    @auth.login_required
    def post(self):
        post_json = post_data.parse_args()
        comments_post = Comments(
            uid = g.user.id,
            create_time = datetime.now(),
            post_id = post_json['post_id'],
            post_type = post_json['post_type'],
            content = post_json['content']
        )
        db.session.add(comments_post)
        db.session.commit()
        return Resp(msg='提交成功').json