# coding: utf-8
class SCNode:
    def __init__(self,item):
        self.data=item
        self.next=None

class SinCirLinkList:
    def __init__(self,node=None):
        self.__head=node
        if node:
            self.__head.next=self.__head
            # or node.next=node
    
    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.__head==None:
            return 0
        cur=self.__head
        count=1
        while cur.next!=self.__head:
            cur=cur.next
            count+=1
        return count
        
    def travel(self):
        if self.__head == None:
            return
        cur=self.__head
        count=1
        while count<2:
            if cur.next==self.__head:
                count+=1
            print(cur.data,end=" ")
            cur=cur.next
        print("")

        # 有时间复现一下视频里的思路

    def add(self,item):
        node=SCNode(item)
        if self.__head == None:
            self.__head=node
            node.next=node
        else:
            # 1 先找到最后一个节点，即循环后的cur
            cur=self.__head
            while cur.next != self.__head:
                cur=cur.next
            
            # 2 再完成头插
            node.next=self.__head
            self.__head=node

            # 3 最后实现回环
            cur.next=self.__head

    def append(self,item):
        node=SCNode(item)
        if self.__head == None:
            self.__head=node
            node.next=node
        else:
            # 1 先找到最后一个节点，即循环后的cur
            cur=self.__head
            while cur.next != self.__head:
                cur=cur.next
            
            # 2 完成尾插，并且更新回环
            node.next=self.__head
            cur.next=node
            
    def insert(self,pos,item):
        if pos <=0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            node=SCNode(item)

            # 1 定位到目标节点以及前一个节点，即为循环后的cur和pre
            pre=None
            cur=self.__head
            while cur.data != item:
                pre=cur
                cur=cur.next
            
            # 2 完成insert
            node.next=cur
            pre.next=node

    def remove(self,item):
        # 是否为空链表
        if self.__head != None:

            # 假设第一个节点为待删除元素
            if self.__head.data==item:
                # 假设当前链表就一个节点
                if self.__head.next==None:
                    self.__head=None
                    return
                else:
                    # 1 将链表头指向下一个节点
                    self.__head=self.__head.next
                    # 2 完成回环修改
                    cur = self.__head
                    while cur.next != self.__head:
                        cur=cur.next
                    cur.next=self.__head
                    return

            # 假设待删除节点不是第一个与最后一个
            pre=None
            cur=self.__head
            while cur.next != self.__head:
                if cur.data==item:
                    if cur!=self.__head:
                        pre.next=cur.next
                        return
                pre=cur
                cur=cur.next
            
            # 假设待删除节点是第一个
            if cur.data==item:
                pre.next=cur.next

    def search(self,item):
        if self.__head == None:
            return False
        
        cur=self.__head
        while cur.next != self.__head:
            if cur.data==item:
                return True
            cur=cur.next

        if cur.data==item:
            return True

if __name__ =="__main__":
    ll=SinCirLinkList()
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
