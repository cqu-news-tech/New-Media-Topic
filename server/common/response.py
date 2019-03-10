from flask import jsonify
from common.toolbox import safe_get
import json

class Resp(object):
    STATUS_MSG = {
        '10200': '请求成功',
        '10401': 'token无效',
        '10402': '请求参数错误',
        '10403': '无数据访问权限',
        '10405': '请求方法错误'
    }


    @property
    def json(self):
        return jsonify({
            'status': self.status,
            'msg': self.msg,
            'data': self.data
        })


    def __init__(self, *args, **kwargs):
        self.data = safe_get(args, 0) or kwargs.get('data') or {}
        self.status = safe_get(args, 1) or kwargs.get('status') or 10200
        self.msg = safe_get(args, 2) or kwargs.get('msg') or self.STATUS_MSG[str(self.status)]


    def __repr__(self):
        return "<Resp status=%d, msg=%s, data=%s>" % (self.status, self.msg, json.dumps(self.data))
