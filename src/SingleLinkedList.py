# coding: utf-8

class SingleNode:
    def __init__(self, data):
        self.data=data
        self.next=None

class singleLinkedList:
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
            print(cur.data,end=" ")
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
        node=SingleNode(item)
        # 这个也可以 node.next,self.__head=self.__head,node
        node.next=self.__head
        self.__head=node

    def append(self,item):
        '''链表尾部添加元素，即尾插法'''
        node=SingleNode(item)
        if self.__head == None:
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
            # 默认头插法
            self.add(item)
        elif pos > self.length()-1:
            # 默认尾插法
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<(pos-1):
                pre=pre.next
                count+=1

            node=SingleNode(item)
            node.next=pre.next
            pre.next=node

    def remove(self,item):
        ''''''
        pass

    def search(self,item):
        pass

if __name__ =="__main__":
    ll=singleLinkedList()
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
    ll.travel()
