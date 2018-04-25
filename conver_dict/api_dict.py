import bson
for_wechart={
    'id': (bson.objectid.ObjectId,lambda v: {'id': str(v)})
} 
# 'name':item.name,
# 'price':str(item.price),
# 'sales_price':str(item.price),
# 'attr':item.attr,
# 'specifications':item.specifications,
# 'picture':item.picture, 
# 'sales_num':item.sales_num