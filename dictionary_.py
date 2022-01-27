import logging as lg
lg.basicConfig(filename="dict_logs.txt",level=lg.INFO,format="%(asctime)s:%(levelname)s: %(message)s")

class dictionary_:
    '''Dictionary uses Hash table for its application
     This makes the complexity of retrieving value as o(1) which is highly efficient that iterating'''
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
        self.keys__ = []
        self.values__ = []

    def get_hash(self,key):
        try:
            hash_ = 0
            for i in key:
                hash_ += ord(i)
            return hash_%self.max
        except Exception as e:
            lg.error(e)
    def __setitem__(self, key, value):
        try:
            self.keys__.append(key)
            self.values__.append(value)
            h = self.get_hash(key)
            self.arr[h] = value
        except Exception as e:
            lg.error(e)
    def __getitem__(self, key):
        try:
            h = self.get_hash(key)
            return self.arr[h]
        except Exception as e:
            lg.error(e)
    def __delitem__(self, key):
        try:
            self.keys__.remove(key)
            h = self.get_hash(key)
            self.arr[h] = None
        except Exception as e:
            lg.error(e)
    def keys_(self):
        try:
            return self.keys__
        except Exception as e:
            lg.error(e)
    def values_(self):
        try:
            return [i for i in self.arr if i!=None]
        except Exception as e:
            lg.error(e)
    def get_(self,key):
        try:
            h = self.get_hash(key)
            return self.arr[h]
        except Exception as e:
            lg.error(e)
    def items_(self):
        return [(i,j) for i,j in zip(self.keys__,self.values__)]
    def pop_(self,key):
        try:
            h = self.get_hash(key)
            self.arr[h] = None
            idx = self.keys__.index(key)
            self.values__.pop(idx)
            self.keys__.pop(idx)
        except Exception as e:
            lg.error(e)
    def __repr__(self):
        return str({i:j for i,j in zip(self.keys__,self.values__)})
    def update_(self,dict_:dict):
        try:
            key = dict_.keys()
            value = dict_.values()



            if type(key) == list:
                for k,v in zip(key,value):
                    self.keys__.extend(k)
                    self.values__.extend(v)
                    h = self.get_hash(k)
                    self.arr[h] = v
            else:
                pass
        except Exception as e:
            lg.error(e)



    def clear_(self):
        try:
            self.arr = [None for i in range(self.max)]
            self.keys__ = []
            self.values__ = []
        except Exception as e:
            lg.error(e)








