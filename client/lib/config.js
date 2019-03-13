var restUrl = "https://newmedia.maxoyed.com"
// var restUrl = "http://127.0.0.1:5000"
var userApi = {
   login :'/user/login',
    profile:'/user/profile',
    verify_token:'/user/verify_token',
    mytopic: '/user/mytopic'
}
var planApi = {
    list: "/topic/plan/list",
    detail: "/topic/plan/detail",
    post: "/topic/plan/post",
    review: "/topic/plan/review"
}
var advanceApi = {
    post: "/topic/advance/post"
}
var commentsApi = {
    list: "/topic/comments/list",
    post: "/topic/comments/post"
}
var closeApi = "/topic/close"
var adminApi = {
    user_review: "/user/review"
}

module.exports =  {
    restUrl: restUrl,
    userApi: userApi,
    planApi: planApi,
    advanceApi: advanceApi,
    commentsApi: commentsApi,
    closeApi: closeApi,
    adminApi: adminApi
}