from flask import jsonify
from flask.blueprints import Blueprint


web_law = Blueprint('LAW', __name__)

@web_law.route('/list',methods=['POST'])
def law_list():
    res={'code':0,'msg':'成功','law_id':'129993838',
'result':[{'law_id':'IIJFEIIJ19384','title':'this is a test','law_date':'2018-04-09','sub_title':'this is a sub_title','type':'时政要闻'}]}
    return jsonify(res)

@web_law.route('/info',methods=['GET'])
def law_info():
    res={'code':0,'msg':'成功','result':{'law_id':'xxxijij12312','title':'this is a test','law_date':'2018-2-12','sub_title':'this is a sub_time','content':'<p>this is a html info<p>'}}
    return jsonify(res)

@web_law.route('/mall/discoverList',methods=['POST'])
def discover_list():
    res={'code':0,'msg':'成功','page_total':10,'result':[]}
    return jsonify(res)
