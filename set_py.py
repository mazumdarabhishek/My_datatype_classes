import logging as lg
lg.basicConfig(filename="set_logs.txt",level=lg.INFO,format="%(asctime)s:%(levelname)s: %(message)s")

class set_:
    def __init__(self,input):
        self.input = input
        self._set = {}
    def __repr__(self):
        return str(self._set)
    def make_set(self):
        try:
            if len(self.input) == 1:
                self._set = str({self.input})
            else:
                l = []
                for i in self.input:
                    if i in l:
                        continue
                    else:
                        l.append(i)
            self._set = set(l)
        except Exception as e:
            lg.error(e)
    def difference_(self,s1,s2):
        try:
            l = []
            for i,j in zip(s1,s2):
                if i != j:
                 l.append(i)
                else:
                    continue
            self._set = set(l)
        except Exception as e:
            lg.error(e)
    def copy_(self):
        return self._set
    def clear_(self):
        self._set = {}
    def add_(self,inp):
        try:
            l = []
            if inp in self._set:
                pass
            else:
                l = [i for i in self._set]
                l.append(inp)
                self._set = set(l)
        except Exception as e:
            lg.error(e)
    def difference_update_(self,s):
        l = [i for i in self._set]
        for i in l:
            if i in s:
                l.remove(i)
        self._set = set(l)
    def discard_(self,num):
        try:
            l = [i for i in self._set]
            if num in l:
                l.remove(num)
            else:
                pass
            self._set = set(l)
        except Exception as e:
            lg.error(e)
    def intersection_(self,s1):
        try:
            l = []
            for i in s1:
                if i in self._set:
                    l.append(i)
            return set(l)
        except Exception as e:
            lg.error(e)
    def intersection_update_(self,s1):
        try:
            l = []
            for i in s1:
                if i in self._set:
                    l.append(i)
            self._set = set(l)
        except Exception as e:
            return e
    def is_disjoint(self,s):
        try:
            for i in self._set:
                if i in s:
                    return False
            return True
        except Exception as e:
            lg.error(e)
    def is_subset(self,s):
        try:
            len_1 = len(s)
            len_2 = len(self._set)
            count = 0
            if len_2<len_1:
                for i in self._set:
                    if i in s:
                        count += 1
                if count == len_2:
                    return True
            else:
               return False
        except Exception as e:
            lg.error(e)
    def is_superset(self,s):
        try:
            len_1 = len(s)
            len_2 = len(self._set)
            count = 0
            if len_2>len_1:
                for i in s:
                    if i in self._set:
                        count += 1
                if count == len_1:
                    return True
            else:
               return False
        except Exception as e:
            lg.error(e)
    def pop_(self):
        l = [i for i in self._set]
        l.pop()
        self._set = set(l)
    def remove_(self,val):
        l = [i for i in self._set]
        l.remove(val)
        self._set = set(l)
    def symmetric_diff(self,s):
        try:
            l = []
            for i in s:
                if i in self._set:
                    continue
                else:
                    l.append(i)
            for i in self._set:
                if i in l:
                    continue
                else:
                    l.append(i)
            return set(l)
        except Exception as e:
            lg.error(e)

    def symmetric_diff_update(self,s):
        try:
            l = []
            for i in s:
                if i in self._set:
                    continue
                else:
                    l.append(i)
            for i in self._set:
                if i in l:
                    continue
                else:
                    l.append(i)
            self._set = set(l)
        except Exception as e:
            lg.error(e)
    def union_(self,s):
        try:
            l = [i for i in self._set]
            for i in s:
                if i in l:
                    continue
                else:
                    l.append(i)
            return set(l)
        except Exception as e:
            lg.error(e)

















