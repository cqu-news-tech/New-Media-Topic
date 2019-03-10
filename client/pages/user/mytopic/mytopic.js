// pages/user/mytopic/mytopic.js
import { Base } from '../../../lib/base.js'
import { userApi } from '../../../lib/config.js'
let nm = new Base()
let user_api = userApi
var app = getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
        topics: []
    },
    onShow() {
        this.getList()
        this.setData({
            authdata: app.globalData.authdata
        }
        )
    },

    navToPlan(e) {
        var uid = nm.getDataSet(e, 'uid')
        var post_id = nm.getDataSet(e, 'post_id')
        wx.navigateTo({
            url: '../../topic/plan/plan?uid=' + uid + '&post_id=' + post_id
        })
    },
    changeExpire(e) {
        var uid = nm.getDataSet(e, 'uid')
        var post_id = nm.getDataSet(e, 'post_id')
        var expired = nm.getDataSet(e, 'expired')
        var state = nm.getDataSet(e, 'state')
        var is_admin = this.data.authdata.is_admin
        var action_text = '关闭此选题'
        if (is_admin) {
            console.log('选题状态改变')
            this._postMyTopic(post_id)
        }
        else if (state == 2 && !is_admin) {
            wx.showModal({
                title: '提示',
                content: '选题已审核,无法关闭',
                showCancel: false,
                confirmText: '我知道了',
                confirmColor: '#1296db'
            })
        }
        else if (state != 2 && !is_admin) {
            console.log('选题状态改变')
            this._postMyTopic(post_id)
        }
    },
    _postMyTopic(post_id) {
        nm.request({
            url: user_api.mytopic,
            data: {
                post_id: post_id
            },
            toast: true
        }, res => {
            this.getList()
            this.setData({
                authdata: app.globalData.authdata
            })
        })
    },
    getList() {
        nm.request({
            url: user_api.mytopic,
            data: {},
            method: 'GET'
        }, res => {
            console.log(res)
            this.setData({
                topics: res.data.list
            })
        })
    },
})