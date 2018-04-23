from mongoengine import *

DB_NAME='law'

class News(DynamicDocument):
    meta = {
        'db_alias': DB_NAME,
        'collection': 'news',
        'index_background': True
    }