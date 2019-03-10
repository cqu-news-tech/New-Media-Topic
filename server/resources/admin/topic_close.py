from flask_restful import Resource
from common.models import PostPlan, PostAdvance, admin_required, auth, db
from common.response import Resp

class TopicClose(Resource):
    @auth.login_required
    @admin_required
    def post(self):
        PostPlan.query.filter(PostPlan.is_expired == False).update({'is_expired': True})
        PostAdvance.query.filter(PostAdvance.is_expired == False).update({'is_expired': True})
        db.session.commit()
        return Resp(msg='关闭选题成功').json