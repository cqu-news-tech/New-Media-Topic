// pages/topic/plan.js
import { Base } from '../../../lib/base.js'
import { planApi, advanceApi, commentsApi, userApi } from '../../../lib/config.js'
const app = getApp()
var nm = new Base()
var plan_api = planApi
var advance_api = advanceApi
var comments_api = commentsApi
var user_api = userApi
var options = ''
Page({

    /**
     * 页面的初始数据
     */
    data: {
        plan: {},
        planComments: [],
        advanceComments: [],
        advance: {},
        canEdit: false,
        isAdmin: false,
        currentTab: 1,
        releaseFocus: false,
        post_type: 'plan',
        post_id: 0,
        comment_content: ''
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (option) {
        options = option
    },
    onShow() {
        console.log(options)
        this.refresh(options)
    },
    onShareAppMessage() {
        return {
            title: '我分享了选题：[' + this.data.plan.title + ']，快来一起看看吧！'
        }
    },
    bindReply: function (e) {
        this.setData({
            releaseFocus: !this.data.releaseFocus
        })
    },
    postComment() {
        var comment_data = {
            post_type: this.data.post_type,
            post_id: this.data.post_id,
            content: this.data.comment_content
        }
        console.log(comment_data)
        nm.request({
            url: comments_api.post,
            data: comment_data
        }, res => {
            this.setData({
                comment_content: '',
                releaseFocus: false
            })
            this.refresh(options)
        })
    },
    // tab切换
    switchTab(e) {
        if (nm.getDataSet(e, 'tab') == 1) {
            this.setData({
                post_type: 'plan',
                post_id: this.data.plan.post_id ? this.data.plan.post_id : ''
            })
        } else {
            this.setData({
                post_type: 'advance',
                post_id: this.data.advance.post_id ? this.data.advance.post_id : ''
            })
        }
        this.setData({
            currentTab: nm.getDataSet(e, 'tab'),
            releaseFocus: false
        })
    },
    // 获取评论输入数据
    inputComment(e) {
        this.setData({
            comment_content: e.detail.value
        })
    },
    // 获取输入数据
    inputText(e) {
        var post_type = nm.getDataSet(e, 'post_type')
        var name = nm.getDataSet(e, 'name')
        var temp = this.data[post_type]
        temp[name] = e.detail.value
        this.setData({
            [post_type]: temp
        })
    },
    bindDateChange: function (e) {
        var advance = this.data.advance
        advance.finish_time = e.detail.value
        console.log('picker发送选择改变，携带值为', e.detail.value)
        this.setData({
            advance: advance
        })
    },
    // 提交选题
    postPlan() {
        let that = this
        var data = {
            post_id: this.data.plan.post_id,
            state: this.data.plan.state == 3 ? 1 : this.data.plan.state,
            title: this.data.plan.title,
            content: this.data.plan.content
        }

        nm.request({
            url: plan_api.post,
            data: data,
            tips: '正在提交'
        }, res => {
            console.log(res)
            this.refresh(options)
        })
    },
    // 提交选题推进
    postAdvance() {
        var that = this
        var data = {
            post_id: that.data.advance.post_id,
            uid: options.uid,
            plan_id: that.data.plan.post_id,
            director: that.data.advance.director,
            finish_time: that.data.advance.finish_time,
            read_num: that.data.advance.read_num,
            content: that.data.advance.content
        }
        console.log(data)
        nm.request({
            url: advance_api.post,
            data: data,
            tips: '正在提交…'
        }, res => {
            console.log(res)
            this.refresh(options)
        })
    },
    // 提交审核
    review(e) {
        let that = this
        let is_expired = nm.getDataSet(e, 'expire')
        var expire_text = is_expired ? '开启此选题' : '关闭此选题'
        wx.showActionSheet({
            itemList: ['通过', '未通过', expire_text],
            success: function (res) {
                var state = 1
                switch (res.tapIndex) {
                    case 0:
                        state = 2
                        break
                    case 1:
                        state = 3
                        break
                    case 2:
                        nm.request({
                            url: user_api.mytopic,
                            data: {
                                post_id: that.data.plan.post_id,
                            },
                            tips: '正在提交…'
                        }, res => {
                            that.refresh(options)
                        })
                        break
                }
                if (res.tapIndex != 2) {
                    nm.request({
                        url: planApi.review,
                        data: {
                            post_id: that.data.plan.post_id,
                            state: state
                        },
                        tips: '正在提交…'
                    }, res => {
                        that.refresh(options)
                    })
                }
            }
        })
    },
    // 刷新页面
    refresh(options) {
        console.log('刷新中')
        nm.request({
            url: plan_api.detail,
            data: options
        }, res => {
            console.log(res)
            this.setData({
                plan: res.data.plan,
                advance: res.data.advance,
                canEdit: res.data.can_edit,
                post_id: res.data.plan.post_id
            })
            nm.request({
                url: comments_api.list,
                data: {
                    post_id: res.data.plan.post_id ? res.data.plan.post_id : 0,
                    post_type: 'plan',
                },
                tips: '加载评论中…'
            }, ress => {
                this.setData({
                    planComments: ress.data.list.length == 0 ? false : ress.data.list
                })
            })
            nm.request({
                url: comments_api.list,
                data: {
                    post_id: res.data.advance.post_id ? res.data.advance.post_id : 0,
                    post_type: 'advance'
                },
                tips: '加载评论中…'
            }, ress => {
                console.log(ress.data.list)
                this.setData({
                    advanceComments: ress.data.list.length == 0? false : ress.data.list
                })
            })
        })
        this.setData({
            isAdmin: app.globalData.authdata.is_admin
        })
    }
})