import json
from flask import jsonify,request
from flask.blueprints import Blueprint
from services.shop_s import ShopService 


api_shop = Blueprint('SHOP', __name__)


@api_shop.route('/discoverlist',methods=['POST'])
def discover_list():
    param = json.loads(request.data.decode("utf-8")) 
    offset=param.get('offset',0)
    size=param.get('size',10)
    data,count=ShopService().get_shop_list(offset,size)
    res={
        'code':0,
        'msg':'成功',
        'total_count':count,
        'result':data
    }
    return jsonify(res)

@api_shop.route('/adlist',methods=['GET'])
def adver_list():
    res=[{'pic_url':'../images/top_3.jpeg'},{'pic_url':'../images/top_4.jpeg'},{'pic_url':'../images/top_5.jpeg'}]
    result={'code':0,'msg':'','result':res}
    return jsonify(result)

@api_shop.route('/host/list',methods=['POST'])
def get_host_list():
    param = json.loads(request.data.decode("utf-8")) 
    res={
        'code':-1,
        'msg':'接口正在开发中',
        'result':{}
    }
    return jsonify(res)
