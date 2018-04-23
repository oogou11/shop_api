from mongoengine import *
from datetime import datetime

class Product(DynamicDocument):
    meta = { 
        'collection': 'product',
        'index_background': True
    }
    name=StringField() #产品名称
    price=DecimalField() #实际价格
    sales_price=DecimalField() #销售价格
    attrs=ListField()          #属性
    specifications=StringField() #规格
    picture=StringField()  #图片地址
    public_time=DateTimeField(default=datetime.now())