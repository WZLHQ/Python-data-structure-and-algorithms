# we implement ADT stack with List

class Stack:
    # 把List的末端当作栈的顶，这样push和pop操作都是O(1)的时间复杂度
    # List每个方法的复杂度可以查阅资料获取
    def __init__(self):
        self.list=[]

    def stack(self):
        return self.list
    
    def push(self,item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)

class Stack_:
    # 把List的首端当作栈顶，这样push和pop的时间复杂度均为O(N)
    def __init__(self):
        self.list=[]

    def stack(self):
        return self.list
    
    def push(self,item):
        self.list.insert(0,item)
    
    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)
