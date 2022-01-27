import logging as lg
lg.basicConfig(filename="list_logs.txt",level=lg.INFO,format="%(asctime)s:%(levelname)s: %(message)s")
class list_:
    def __init__(self,l):
        self.l = l
        self.len = len(self.l)
    def append_(self,input):
        self.l[len(self.l):]= [input]
        return None
    def clear_(self):
        self.l = []
        return None
    def copy_(self):
        return self.l
    def count_(self,input):
        counter = 0
        for i in self.l:
            if i == input:
                counter +=1
        return counter
    def extend_(self,extender=[]):
        self.l[len(self.l):] = extender

    def  index_(self,input):
        for i in range(self.l):
            if self.l[i] == input:
                return i
        else:
            return None
    def insert_(self,loc,input):
        first_half = self.l[:loc]
        second_half = self.l[loc+1:len(self.l)-1]
        first_half[len(first_half):] = [input]
        first_half[len(first_half):] = second_half
        self.l = first_half
    def pop_(self,idx=None):
        if idx == None:
            idx = len(self.l)
            pop_num = self.l[idx-1]
            self.l = self.l[:idx-1]
            return pop_num
        else:
            if idx ==0:
                pop_num = self.l[idx]
                self.l = self.l[idx + 1:]
                return pop_num
            elif idx > 0:
                pop_num = self.l[idx]
                f = self.l[:idx]
                s = self.l[idx+1:]
                self.l = f + s
                return pop_num
            elif idx >= len(self.l):
                lg.error("index out of range")
                raise IndexError("index out of range")
            elif idx < 0 :
                lg.error("No such index exists")
                raise IndexError("No such index exists")

    def remove_(self,input):
        try:
            for i in self.l:
                if i == input:
                    self.pop_(input)
        except Exception as e:
            lg.error(e)

    def reverse_(self):
        try:
            self.l = self.l[::-1]
        except Exception as e:
            lg.error(e)
    def sort_(self):
        try:
            if type(self.l[0])==int:
                for iter_num in range(len(self.l) - 1, 0, -1):
                    for idx in range(iter_num):
                        if self.l[idx] > self.l[idx + 1]:
                            temp = self.l[idx]
                            self.l[idx] = self.l[idx + 1]
                            self.l[idx + 1] = temp
            elif type(self.l[0])==str:
                temp_dict = {}
                for i in self.l:
                    temp_dict[ord(i[0])] = i
                result = []
                for j in sorted(temp_dict.keys()):
                    result.append(temp_dict[i])
                self.l = result

        except:
            lg.error('cannot compare str with int')
            raise ValueError('cannot compare str with int')

    def print_list(self):
        return self.l


















