import json
from flask import jsonify,request
from flask.blueprints import Blueprint

api_search = Blueprint('SEARCH', __name__) 


@api_search.route('/list',methods=["GET"])
def search_words():
    openid=request.args.get('openId') 
    result={'code':-1,'msg':'接口正在开发中','result':{}}
    return jsonify(result)

@api_search.route('/add',methods=["POST"])
def add_workds(): 
    param = json.loads(request.data.decode("utf-8"))
    openid=param.get('openid',None),
    keyword=param.get('keyword',None)
    result={'code':-1,'msg':'接口正在开发中','result':{}}
    return jsonify(result)

@api_search.route('/clear',methods=["GET"])
def clear_workds():  
    openid=request.args.get('openId') 
    result={'code':-1,'msg':'接口正在开发中','result':{}}
    return jsonify(result)