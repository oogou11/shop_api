import json
import hashlib
from flask import jsonify,request
from flask.blueprints import Blueprint

api_wechart = Blueprint('WECHART', __name__) 


@api_wechart.route('/online/customer',methods=["GET"])
def wechart_token(): 
    token='5ad5cfd774da54e0b34da1da'
    signature=request.args.get('signature')
    echostr=request.args.get('echostr')
    timestamp=request.args.get('timestamp')
    timestamp=request.args.get('timestamp')
    nonce=request.args.get('nonce')
    arr=[token,timestamp,nonce]
    hd_arr=sorted(arr)
    hash = hashlib.sha1()
    hd_str=''.join(map(str, hd_arr))
    hash.update(hd_str.encode('utf-8'))
    hsh_result=hash.hexdigest()
    print(hsh_result,signature)
    if hsh_result==signature:
        return echostr
    else:
        return None