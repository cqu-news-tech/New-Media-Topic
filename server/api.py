from resources.user.login import Login as user_login
from resources.user.profile import Profile as user_profile
from resources.user.verify_token import VerifyToken as user_verify_token
from resources.user.mytopic import MyTopic as user_mytopic
from resources.admin.user_review import UserReview as user_review

from resources.admin.topic_close import TopicClose as topic_close
from resources.topic.plan_list import PlanList as topic_plan_list
from resources.topic.plan_detail import PlanDetail as topic_plan_detail
from resources.topic.plan_post import PLanPost as topic_plan_post
from resources.admin.plan_review import PlanReview as topic_plan_review

from resources.topic.advance_post import AdvancePost as topic_advance_post

from resources.topic.comments_list import CommentsList as topic_comments_list
from resources.admin.comments_post import CommentsPost as topic_comments_post



from common.models import app, api

api.add_resource(user_login, '/user/login')
api.add_resource(user_profile, '/user/profile')
api.add_resource(user_verify_token, '/user/verify_token')
api.add_resource(user_review, '/user/review')

api.add_resource(user_mytopic, '/user/mytopic')

api.add_resource(topic_close, '/topic/close')
api.add_resource(topic_plan_list, '/topic/plan/list')
api.add_resource(topic_plan_detail, '/topic/plan/detail')
api.add_resource(topic_plan_post, '/topic/plan/post')
api.add_resource(topic_plan_review, '/topic/plan/review')
api.add_resource(topic_advance_post, '/topic/advance/post')
api.add_resource(topic_comments_list, '/topic/comments/list')
api.add_resource(topic_comments_post, '/topic/comments/post')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)