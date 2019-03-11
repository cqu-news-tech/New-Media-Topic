from common.models import app, User
from flask_restful import Resource, reqparse
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from common.response import Resp
post_data = reqparse.RequestParser()
post_data.add_argument('token', type=str)

class VerifyToken(Resource):
    def post(self):
        post_json = post_data.parse_args()
        token = post_json['token'][7:]
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
            user = User.query.get(data['id'])
            if user:
                res = {
                    "token": 'Bearer ' + token,
                    "is_verify": user.is_verify,
                    "is_register": user.is_register,
                    "is_admin": user.is_admin
                }
            else:
                return Resp(status=10401, msg='token无效').json
        except SignatureExpired:
            return Resp(status=10401, msg='token过期').json  # valid token, but expired
        except BadSignature:
            return Resp(status=10401, msg='token无效').json  # invalid token
        return Resp(res, msg='token有效').json