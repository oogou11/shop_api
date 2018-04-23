import requests

class UserService(object):
    
    def __init__(self):
        self.url='https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'
     
    def get_session_key(self,code):
        url=self.url.formate('1','2',code)
