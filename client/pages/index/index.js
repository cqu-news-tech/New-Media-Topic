//index.js
//获取应用实例
import { Base } from '../../lib/base.js'
import { planApi } from '../../lib/config.js'
import { Token } from '../../lib/token.js'
var token = new Token()
const app = getApp()
var nm = new Base()
var plan_api = planApi
Page({
    data: {
        topic: [],
        currentTab: 1
    },
    onShow() {
        this.refresh()
    },
    onPullDownRefresh(){
        this.refresh(res => {
            wx.stopPullDownRefresh()
        })
    },
    switchTab(e) {
        this.setData({
            currentTab: nm.getDataSet(e, 'tab')
        })
    },
    navToPlan(e) {
        var uid = nm.getDataSet(e, 'uid')
        var post_id = nm.getDataSet(e, 'post_id')
        wx.navigateTo({
            url: '../topic/plan/plan?uid=' + uid + '&post_id=' + post_id
        })
    },
    refresh(callback){
        token.verify(res => {
            console.log(res)
            app.globalData.authdata = res
            if (res.is_register == false) {
                wx.navigateTo({
                    url: '../user/register/register',
                })
            }
            else if (res.is_verify == false) {
                wx.navigateTo({
                    url: '../user/verify/verify',
                })
            }
            this._getList()
            callback && callback(res)
        })
    },
    _getList(){
        nm.request({
            url: plan_api.list,
            method: 'GET',
            toast: false
        }, res => {
            console.log(res)
            this.setData({
                topic: res.data.list
            })
        })
    },
    onShareAppMessage(){}
})
