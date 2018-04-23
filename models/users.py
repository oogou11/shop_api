from datetime import datetime
from mongoengine import *

class Users(DynamicDocument):
    meta = { 
        'collection': 'users',
        'index_background': True
    }
    openid=StringField()
    expires_in=IntField()
    session_key=StringField()
    nickName=StringField()
    avatarUrl=StringField()
    gender=IntField() #性别 0：未知、1：男、2：女
    city=StringField()
    province=StringField()
    country=StringField()
    language=StringField()
    create_time=DateTimeField(default=datetime.now())