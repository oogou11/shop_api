from mongoengine import *
from datetime import datetime
from shop import Product

class Comments(DynamicDocument):
    meta = { 
        'collection': 'comments',
        'index_background': True
    } 
    avatarUrl=StringField() #头像 
    openId=StringField() #openid
    content=StringField() #评论内容
    start=IntField() #评级
    children=ListField() #回复
    product=ReferenceField(Product) #productId
    time=DateTimeField(default=datetime.now())