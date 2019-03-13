import { restUrl, userApi } from './config.js'
class Token {
    constructor() {
        this.verifyUrl = restUrl + userApi.verify_token;
        this.tokenUrl = restUrl + userApi.login;
    }

    verify(callback) {
        var that = this
        wx.getStorage({
            key: 'authdata',
            success: function (res) {
                that._veirfyFromServer(res.data, callback);
            },
            fail: function (res) {
                that.getTokenFromServer(callback);
            }
        })
    }

    _veirfyFromServer(authdata, callback) {
        var that = this;
        wx.request({
            url: that.verifyUrl,
            method: 'POST',
            data: {
                token: authdata.token
            },
            success: function (res) {
                console.log(res.data)
                if (res.data.status != 10200) {
                    that.getTokenFromServer(callback);
                } else {
                    wx.setStorage({
                        key: 'authdata',
                        data: res.data.data,
                        success: function (data) {
                            callback && callback(res.data.data);
                        }
                    })
                }
            }
        })
    }

    getTokenFromServer(callback) {
        var that = this;
        wx.login({
            success: function (res) {
                wx.request({
                    url: that.tokenUrl,
                    method: 'POST',
                    data: {
                        code: res.code
                    },
                    success: function (res) {
                        
                        if (res.data.status == 10200) {
                            wx.setStorage({
                                key: 'authdata',
                                data: res.data.data,
                                success: function (e) {
                                    callback && callback(res.data.data);
                                }
                            })
                        }
                        else {
                            wx.showToast({
                                title: res.data.msg,
                                icon: 'none',
                                duration: 800
                            })
                        }
                    }
                })
            },
            fail(err){
                console.log(err)
            }
        })
    }
}

module.exports = {
    Token: Token
}