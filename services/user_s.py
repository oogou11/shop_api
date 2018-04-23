import requests
import json
from config  import Tencet
from common.singleton import Singleton
from models.users import Users

class UserService(metaclass=Singleton):
    
    def __init__(self):
        self.url='https://api.weixin.qq.com/sns/jscode2session'
     
    def get_session_key(self,code):
        payload={
            'appid':Tencet.get('appid'),
            'secret':Tencet.get('secret'),
            'js_code':code,
            'grant_type':'authorization_code'
        } 
        r=requests.get(self.url,params=payload)
        msg=r.text
        return json.loads(msg)
    
    def save_user(self,code,userinfo):
        tencert_info=self.get_session_key(code)  
        openid=tencert_info.get('openid',None)
        userinfo={**userinfo,**tencert_info} 
        if openid:
            data=self.get_user_by_openid(openid)
            if not hasattr(data,'id'): 
                data=Users()
            for k,v in userinfo.items():
                setattr(data,k,v)
            data.save() 
        else:
            return '-1','7200'
        
        return str(data.id),data.expires_in
    
    def get_user_by_openid(self,openid):
        user=Users.objects(openid=openid).first()
        return user