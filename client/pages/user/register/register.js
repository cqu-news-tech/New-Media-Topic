// pages/register/register.js
import { Base } from '../../../lib/base.js'
import { userApi } from '../../../lib/config.js'
const app = getApp()
var nm = new Base()
var user_api = userApi
Page({

    /**
     * 页面的初始数据
     */
    data: {
        name: '',
        phone: ''
    },
    onLoad(){
        nm.request({
            url: user_api.profile,
            data: this.data,
            method: 'GET'
        }, res => {
            console.log(res)
            this.setData({
                name: res.data.name,
                phone: res.data.phone
            })
        })
    },
    postProfile() {
        if (!this.data.name || !this.data.phone) {
            wx.showToast({
                title: '姓名和手机号不能为空',
                icon: 'none',
                duration: 600,
                mask: true
            })
        } else {
            nm.request({
                url: user_api.profile,
                data: this.data
            }, res => {
                wx.switchTab({
                    url: '../../../pages/index/index'
                })
            })
        }

    },
    inputText(e) {
        var kw = nm.getDataSet(e, 'name')
        var args = e.detail.value
        this.setData({
            [kw]: args
        })
    }
})