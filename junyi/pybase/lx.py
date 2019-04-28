#encoding:utf-8
#空调的类的方法
class air():
    @classmethod
    def refrigeration(self):
        print ("制冷")
    @classmethod
    def heating(self):
        print ("制热")
    @classmethod
    def dehumidification(self):
        print ("除湿")
air.refrigeration()
air.heating()
air().dehumidification()
