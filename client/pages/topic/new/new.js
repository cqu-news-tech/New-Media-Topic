// pages/topic/plan.js
import { Base } from '../../../lib/base.js'
import { planApi, advanceApi, commentsApi } from '../../../lib/config.js'
const app = getApp()
var nm = new Base()
var plan_api = planApi
var advance_api = advanceApi
var comments_api = commentsApi
var options = ''
Page({

    /**
     * 页面的初始数据
     */
    data: {
    },

    /**
     * 生命周期函数--监听页面加载
     */
    // 获取输入数据
    inputText(e) {
        var name = nm.getDataSet(e, 'name')
        this.setData({
            [name]: e.detail.value
        })
    },
    // 提交选题
    postPlan() {
        let that = this
        var data = {
            title: this.data.title,
            content: this.data.content
        }
        nm.request({
            url: plan_api.post,
            data: data,
            tips: '正在提交',
            toast: false
        }, res => {
            console.log(res)
            wx.showToast({
                title: '提交选题成功',
                icon: 'none',
                duration: 600,
                mask: true,
                complete: function (res) {
                    wx.switchTab({
                        url: '../../../pages/index/index',
                        success: function (res) {
                        }
                    })
                },
            })

        })
    }
})