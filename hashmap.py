import time
print("implment a hashmap")
class Hashmap:
    def __init__(self):
        self.len = 6
        self.map = [None] *self.len
    def __get_index__(self,key):
        hash = 0
        for char in str(key):
            hash+=ord(char)
        return hash%self.len

    def add(self,key,value):
        index = self.__get_index__(key)
        if self.map[index] is None:
            self.map[index] = [list([key,value])]
            return True
        else:
            valueInserted = False
            for eachItem in self.map[index]:
                if eachItem[0]==key:
                    eachItem[1] = value
                    valueInserted=True
                    return True
            if not valueInserted:
                self.map[index].append(list([key,value]))
                return True

    def remove(self,key):
        index = self.__get_index__(key)
        if self.map[index] is None:
            return None
        for i in range(0,len(self.map[index])):
            if self.map[index][i][0]==key:
                self.map[index].pop(i)
                return True

    def print(self):
        print("------START------")
        for eachItem in self.map:
            print(eachItem)
        print("------END-------")


h = Hashmap()
h.add("1",1)
h.print()
h.add("10",1)
h.print()
h.add("1",2)
h.print()
h.add("2",2)
h.print()
h.add("20",2)
h.print()
h.add("200",2)
h.print()
h.add("2",4)
h.print()
h.add("blah",2)

h.print()
print("AFTER ALL ADDS")
h.remove("2")
h.print()
h.remove("1")
h.print()
h.remove("10")
h.print()
h.add("1",1)
h.print()