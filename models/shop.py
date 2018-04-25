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
    logo=StringField() #logo
    sales_num=IntField() #销量
    stock_num=IntField() #库存
    photo_list=ListField() #图片
    start_time=DateTimeField() #活动开始时间
    end_time=DateTimeField() #活动结束时间
    public_time=DateTimeField(default=datetime.now())