from flask_restful import Resource, reqparse
from common.models import Comments, User
from common.response import Resp

post_data = reqparse.RequestParser()
post_data.add_argument('post_id', type=int)
post_data.add_argument('post_type', type=str)


class CommentsList(Resource):
    def post(self):
        post_json = post_data.parse_args()
        if post_json['post_id'] == 0:
            return Resp({"list":[]}).json
        comments_list = Comments.query.filter(
            Comments.post_id == post_json['post_id'],
            Comments.post_type == post_json['post_type']
        ).all()
        temp = []
        if comments_list:
            for item in comments_list:
                temp.append({
                    "name": User.query.get(item.uid).name,
                    "content": item.content,
                    "create_time": item.create_time.strftime('%Y-%m-%d %H:%M:%S')
                })
        data = {
            "list": temp
        }
        return Resp(data, msg='评论加载完成').json