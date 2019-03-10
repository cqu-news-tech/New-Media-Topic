from flask_restful import Resource
from common.models import PostPlan, User, auth
from common.response import Resp


class PlanList(Resource):
    def get(self):
        user_list = User.query.all()
        post_list = PostPlan.query.filter_by(is_expired = False).all()
        temp = []
        for user in user_list:
            is_found = False
            for item in post_list:
                if item.uid == user.id:
                    is_found = True
                    temp.append({
                        "post_id": item.id,
                        "uid": item.uid,
                        "create_time": item.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                        "state": item.state,
                        "name": user.name,
                        "title": item.title,
                        "content": item.content
                    })

            if is_found == False:
                temp.append({
                    "post_id": '',
                    "uid": user.id,
                    "create_time": '',
                    "state": 0,
                    "name": user.name,
                    "title": '',
                    "content": ''
                })
        data = {
            "list": temp
        }
        return Resp(data, msg='获取选题列表成功').json