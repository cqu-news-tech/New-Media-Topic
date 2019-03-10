// pages/verify/verify.js
import { Token } from '../../../lib/token.js'
var token = new Token()
const app = getApp()
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
  },
  verify(){
      token.verify(res => {
          app.globalData.authdata = res
          console.log('Launch')
          if (res.is_verify == true) {
              wx.showToast({
                  title: '审核通过',
                  icon: 'none',
                  duration: 800,
                  mask: true,
                  success(){
                      wx.switchTab({
                          url: '../../../pages/index/index',
                      })
                  }
              })
              
          } else {
              wx.showToast({
                  title: '用户身份审核中',
                  icon: 'none',
                  duration: 800,
                  mask: true,
              })
          }
      })
  }
})