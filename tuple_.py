import logging as lg
lg.basicConfig(filename="tup_logs.txt",level=lg.INFO,format="%(asctime)s:%(levelname)s: %(message)s")

class tuple_:
    def __init__(self,*tup):
        self.tup = list(tup)

    def __getitem__(self, item):
        return self.tup[item]
    def count_(self,val):
        try:
            count = 0
            for i in self.tup:
                if i == val:
                    count +=1
            return count
        except Exception as e:
            lg.error(e)
    def index_(self,val):
        try:
            for i in range(len(self.tup)):
                if self.tup[i]==val:
                    return i
            else:
                return 'Not Found'
        except Exception as e:
            lg.error(e)
    def __repr__(self):
        return str(tuple(self.tup))








