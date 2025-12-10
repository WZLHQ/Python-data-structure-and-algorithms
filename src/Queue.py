
class Queue:

    def __init__(self):
        self.list=[]

    def queue(self):
        return self.list

    def enqueue(self,item):
        self.list.insert(0,item)

    def dequeue(self):
        return self.list.pop()

    def isEmpty(self):
        return self.list == []
    
    def size(self):
        return len(self.list)
