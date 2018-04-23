import json
from flask import jsonify,request
from flask.blueprints import Blueprint


api_user = Blueprint('USER', __name__)

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
    print(param)
    res={
	'code':0,
	'msg':'成功',
	'result':{'openid':'oeuj50KHMqsh5kYZYWQJuwmY5yG0','expires_in':'7200'}
    }
    return jsonify(res)
