import json
import os
from flask import jsonify,request,make_response
from flask.blueprints import Blueprint

api_image = Blueprint('IMAGE', __name__) 


@api_image.route('/<pathname>/<name>.jpeg',methods=["GET"])
def get_image(pathname,name): 
    file_path = os.path.join(os.getcwd(), 'statics/{}/{}.jpeg'.format(pathname,name))
    img_content = 'image/jpeg'
    with open(file_path,'rb') as f:
        img = f.read() 
    response = make_response(img)
    response.headers['Content-Type'] = img_content
    return response