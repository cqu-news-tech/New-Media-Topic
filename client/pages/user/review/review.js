// pages/review/review.js
import { Base } from '../../../lib/base.js'
import { adminApi } from '../../../lib/config.js'
const app = getApp()
var nm = new Base()
var admin_api = adminApi
Page({

    /**
     * 页面的初始数据
     */
    data: {

    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        this.refresh()
    },
    userReview(e) {
        let uid = nm.getDataSet(e, 'uid')
        nm.request({
            url: admin_api.user_review,
            data: {
                uid: uid
            },
            toast: true
        }, res => {
            this.refresh()
        })
    },
    refresh(callback) {
        nm.request({
            url: admin_api.user_review,
            data: {},
            method: 'GET'
        }, res => {
            console.log(res)
            callback && callback(res)
            this.setData({
                userList: res.data.list.length == 0 ? false : res.data.list
            })
        })
    },
    onPullDownRefresh(){
        this.refresh(res => {
            wx.stopPullDownRefresh()
        })
    }
})