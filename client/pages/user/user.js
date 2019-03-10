// pages/user/user.js
import { Base } from '../../lib/base.js'
import { closeApi } from '../../lib/config.js'
var close_api = closeApi
var nm = new Base()
var app = getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
        authdata: ''
    },
    onShow() {
        this.setData({
            authdata: app.globalData.authdata
        })
    },
    navTo(e) {
        var url = nm.getDataSet(e, 'url')
        wx.navigateTo({
            url: url,
        })
    },
    closeTopic() {
        wx.showModal({
            title: '提示',
            content: '确认关闭本次选题？',
            showCancel: true,
            confirmText: '嗯。',
            confirmColor: '#1296db',
            cancelText: '点错了',
            cancelColor: '#bfbfbf',
            success: function (res) {
                console.log(res)
                if (res.confirm) {
                    nm.request({
                        url: close_api,
                        data: {},
                        tips: '关闭选题中…'
                    }, res => {
                        console.log(res)
                    })
                }
            }
        })
    }
})