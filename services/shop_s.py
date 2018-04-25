import config
from models.shop import Product 
from common.singleton import Singleton
from decimal import Decimal 

class ShopService(metaclass=Singleton):  

    def get_shop_list(self,offset,size):
        result=[] 
        data=Product.objects().order_by('-id').skip(offset).limit(size) 
        for item in data:
            single={
                'id':str(item.id),
                'name':item.name,
                'price':str(item.price),
                'sales_price':str(item.sales_price),
                'attr':item.attr,
                'specifications':item.specifications,
                'picture':config.HOST+item.picture,
                'logo':config.HOST+item.logo,
                'sales_num':item.sales_num
            }
            result.append(single) 
        return result,data.count()

    def get_shop_detail(self,id):  
        item=Product.objects(id=id).first()
        single={
                'id':id,
                'name':item.name,
                'price':str(item.price),
                'sales_price':str(item.sales_price),
                'attr':item.attr,
                'specifications':item.specifications,
                'picture':config.HOST+item.picture, 
                'logo':config.HOST+item.logo,
                'sales_num':item.sales_num,
                'stock_num':item.stock_num,
                'photo_list':[config+HOST+item for item in item.photo_list],
                'start_time':item.start_time,
                'end_time':item.end_time,
                'goodsSkuNameList':[],
                'detailInfo':{
                    'nodes':[]
                }
            }
        return single
    
    def get_hot_list(self,id,offset,size):   
        info=self.get_shop_detail(id) 
        p_list,count=self.get_shop_list(offset,size)
        return info,p_list,count
