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
                'sales_price':str(item.price),
                'attr':item.attr,
                'specifications':item.specifications,
                'picture':item.picture 
            }
            result.append(single) 
        return result,data.count()

    def get_shop_detail(self,id):  
        data=Product.objects(id=id).first()
        single={
                'id':str(item.id),
                'name':item.name,
                'price':str(item.price),
                'sales_price':str(item.price),
                'attr':item.attr,
                'specifications':item.specifications,
                'picture':item.picture 
            }
        return single
