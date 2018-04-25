api_param_to_where={
    'id':(str,lambda v:{'id':{'$lt':id}} if v else {}),
    'size':(int,lambda v:{'size':v}),
    'sort':(int,lambda v:)
}