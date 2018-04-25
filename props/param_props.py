from common.singleton import Singleton

class ParamProps(metaclass=Singleton):

    def get_sort(self,v):
        if v==1:
            data='-id'
        else:
            data=''
        return data