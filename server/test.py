from common.models import PostPlan, User


post_plan = PostPlan.query.filter(PostPlan.is_expired == False).all()
for item in post_plan:
    user = User.query.get(item.uid)
    print(user.name, item.title, item.content)