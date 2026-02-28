
class Queue:
    def __init__(self):
        self.list=[]

    def enqueue(self, item):
        self.list.append(item)
    
    def isEmpty(self):
        return self.list==[]
    
    def dequeue(self):
        return self.list.pop(0) if not self.isEmpty() else None

    def size(self):
        return self.list
    