import { Token } from './token.js';
import { restUrl } from './config.js';

class Base {
    constructor() {
        this.rest_url = restUrl;
        this.token = new Token();
    }
    request(params, callback) {
        var that = this
        console.log(params)
        wx.showLoading({
            title: params.tips ? params.tips : '正在加载…',
            mask: true
        })
        wx.request({
            url: that.rest_url + params.url,
            data: params.data,
            method: params.method ? params.method : 'POST',
            header: {
                'content-type': 'application/json',
                'Authorization': wx.getStorageSync('authdata').token
            },
            success: function (res) {
                if (res.data.status == 10200) {
                    callback && callback(res.data);
                }
                if (res.data.status == 10401) {
                    that._refetch(params);
                }
                wx.hideLoading()
                if (params.toast == true) {
                    wx.showToast({
                        title: params.toast_text ? params.toast_text : res.data.msg,
                        icon: 'none',
                        duration: 600
                    })
                }

            },
            fail: function (err) {
                that._processError(err);
            }
        })

    }

    _processError(err) {
        console.log(err);
    }

    _refetch(param) {
        var that = this
        this.token.getTokenFromServer((token) => {
            this.request(param);
        });
    }

    /*获得元素上的绑定的值*/
    getDataSet(event, key) {
        return event.currentTarget.dataset[key];
    };

};

module.exports = {
    Base: Base
}
