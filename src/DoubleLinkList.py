# coding: utf-8
class DNode:
    def __init__(self,item):
        self.data=item
        self.pre=None
        self.next=None

class DoubleLinkList:
    def __init__(self,node=None):
        self.__head=node
    
    def is_empty(self):
        pass

    def length(self):
        pass
    
    def travel(self):
        pass

    def add(self,item):
        pass

    def append(self,item):
        pass

    def insert(self,pos,item):
        pass

    def remove(self,item):
        pass

    def search(self,item):
        pass



if __name__ =="__main__":
    ll=DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1,9)
    ll.travel()
    ll.insert(3,100)
    ll.travel()
    ll.insert(10,200)
    print("start")
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()