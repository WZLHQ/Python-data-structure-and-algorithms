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
        return self.__head == None

    def length(self):
        count=0
        cur = self.__head
        while cur != None:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.data, end=" ")
            cur=cur.next
        print(" ")


    def add(self,item):
        # TODO refine this code
        node = DNode(item)
        if self.__head == None:
            self.__head=node
        else:
            node.next=self.__head
            self.__head.pre=node
            self.__head=node

    def append(self,item):
        node=DNode(item)
        if self.__head == None:
            self.__head=node
        else:
            cur = self.__head
            while cur.next != None:
                cur=cur.next
            node.pre=cur
            cur.next=node
            
    def insert(self,pos,item):
        if pos < 0:
            self.add(item)
        elif pos > 0:
            self.append(item)
        else:
            count=0
            node=DNode(item)
            cur=self.__head
            while count<pos:
                cur=cur.next
                count+=1
            node.next=cur
            node.pre=cur.pre
            cur.pre.next=node
            cur.pre=node

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