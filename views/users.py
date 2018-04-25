import json
from flask import jsonify,request
from flask.blueprints import Blueprint
from services.user_s import UserService


api_user = Blueprint('USER', __name__)

service=UserService()

@api_user.route('/getuserinfo',methods=['POST'])
def get_user_info():
    param = json.loads(request.data.decode("utf-8")) 
    openId=param.get('openId',None) 
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)

@api_user.route('/messageInfo',methods=['POST'])
def get_sys_message():
    param = json.loads(request.data.decode("utf-8")) 
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)

@api_user.route('/address/list',methods=['POST'])
def get_address_list():
    param = json.loads(request.data.decode("utf-8")) 
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)

@api_user.route('/address/info',methods=["GET"])
def get_addess_by_id(): 
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)

@api_user.route('/add/address',methods=['PUT'])
def add_address():
    param = json.loads(request.data.decode("utf-8")) 
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)

@api_user.route('/update/address',methods=['POST'])
def update_address():
    param = json.loads(request.data.decode("utf-8")) 
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)

@api_user.route('/jscode2session',methods=['POST'])
def get_session():
    param = json.loads(request.data.decode("utf-8")) 
    code=param.get('jsCode',None)
    userInfo=param.get('userInfo',None)
    if code is None:
        res={
            'code':-1,
            'msg':'非法请求',
            'result':{}
        }
    else:
        openid,expires_in=service.save_user(code,userInfo)
        res={
            'code':0,
            'msg':'成功',
            'result':{
                'openid':openid,
                'expires_in':expires_in
            }
        }
    return jsonify(res)
#用户足迹
@api_user.route('/userbrowse/add',methods=['POST'])
def add_user_browse():
    param = json.loads(request.data.decode("utf-8")) 
    openId=param.get('openId',None)
    product_id=param.get('product_id',None)
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)

