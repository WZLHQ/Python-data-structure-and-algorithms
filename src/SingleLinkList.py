# coding: utf-8

class SNode:
    def __init__(self, data):
        self.data=data
        self.next=None

class singleLinkList:
    '''单链表'''
    def __init__(self,node=None):
        # 开头双下划线表示私有属性
        self.__head=node

    def is_empty(self):
        return self.__head is None

    def length(self):
        '''非递归形式'''
        cur=self.__head
        count=0
        while cur!=None:
            cur=cur.next
            count+=1
        return count
    
        '''递归形式实现的链表长度计算'''
        def get_len(cur):
            if cur==None:
                return 0
            return 1+get_len(cur.next)
        return get_len(self.__head)
    
    def travel(self):
        '''非递归形式'''
        cur=self.__head
        while cur !=None:
            print(cur.data, end=" ")
            cur=cur.next
        print("")

        '''递归形式
        每次调用travel时，travel_print都会被重复调用，可以考虑将其作为私有方法
        '''
        # def travel_print(cur):
        #     if cur ==None:
        #         return
        #     print(cur.data)
        #     travel_print(cur.next)
        # travel_print(self.__head)

    def add(self,item):
        '''链表头部添加元素，即头插法'''
        node=SNode(item)
        # 这个也可以 node.next,self.__head=self.__head,node
        node.next=self.__head
        self.__head=node

    def append(self,item):
        '''链表尾部添加元素，即尾插法'''
        node=SNode(item)
        if self.__head is None:
            self.__head=node
        else:
            cur=self.__head
            while cur.next != None:
                cur=cur.next
            cur.next=node

    def insert(self,pos,item):
        '''
        指定位置添加元素
        pos 从0开始
        '''
        if pos<0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
            node=SNode(item)
            cur=self.__head
            count=0
            while count<(pos-1):
                cur=cur.next
                count+=1
            node.next=cur.next
            cur.next=node

    def remove(self,item):
        '''从头开始，删除第一个符合情况的元素即可退出'''        
        cur=self.__head
        pre=None
        while cur != None:
            if cur.data==item:
                if cur==self.__head:
                    self.__head=self.__head.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next

    def search(self,item):
        '''从头开始查找，找到就返回True，不管后续是否仍然存在'''
        cur=self.__head
        while cur!=None:
            if cur.data==item:
                return True
            else:
                cur=cur.next
        return False



if __name__ =="__main__":
    ll=singleLinkList()
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