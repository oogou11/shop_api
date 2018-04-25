import json
import os
import config
from flask import jsonify,request
from flask.blueprints import Blueprint
from services.shop_s import ShopService 


api_shop = Blueprint('SHOP', __name__)
service=ShopService()


@api_shop.route('/discoverlist',methods=['POST'])
def discover_list():
    param = json.loads(request.data.decode("utf-8")) 
    offset=param.get('offset',0)
    size=param.get('size',10)
    data,count=service.get_shop_list(offset,size)
    res={
        'code':0,
        'msg':'成功',
        'total_count':count,
        'result':data
    }
    return jsonify(res)

@api_shop.route('/adlist',methods=['GET'])
def adver_list(): 
    path='statics/adlist'
    list_name=[]
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.splitext(file_path)[1]=='.jpeg':
            list_name.append(config.HOST+file_path)  
    result={'code':0,'msg':'','result':list_name}
    return jsonify(result)

@api_shop.route('/detail',methods=["GET"])
def get_product_detail():
    product_id=request.args.get('id')
    data=service.get_shop_detail(product_id) 
    result={'code':0,'msg':'成功','result':data}
    return jsonify(result)

@api_shop.route('/host/list',methods=['POST'])
def get_host_list():
    param = json.loads(request.data.decode("utf-8"))
    if 'product_id' not in param:
        res={
        'code':-1,
        'msg':'缺少必要参数',
        'result':{}
        }
        return jsonify(res) 
    product_id=param.get('product_id') 
    offset=param.get('offset',0)
    size=param.get('size',10) 
    info,p_list,count=service.get_hot_list(product_id,offset,size)
    res={
        'code':0,
        'msg':'成功',
        'total_count':count,
        'product':info,
        'result':p_list
    }
    return jsonify(res)
