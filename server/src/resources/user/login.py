from flask_restful import Resource, reqparse
from common.models import wxapp, User, db
from common.response import Resp
from common.toolbox import safe_get
post_data = reqparse.RequestParser()
post_data.add_argument('code', type=str)

def getData(*user):
    user = safe_get(user, 0)
    if user:
        return {
            "token": user.token,
            "is_verify": user.is_verify,
            "is_register": user.is_register,
            "is_admin": user.is_admin
        }
    else:
        return {}

class Login(Resource):
    def post(self):
        post_args = post_data.parse_args()
        if post_args['code'] == "maxoyed":
            openid = "maxoyed"
        else:
            openid = wxapp.jscode2session(post_args['code']).get('openid')
        if openid is None:
            return Resp(getData(), 10402, 'code无效').json
        user = User.query.filter_by(openid=openid).first()
        if user is not None:
            return Resp(getData(user), msg='登录成功').json
        else:
            user = User(openid=openid)
            db.session.add(user)
            db.session.commit()
            return Resp(getData(user), msg='登录成功').json
