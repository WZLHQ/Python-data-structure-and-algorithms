
class Stack:

    def __init__(self):

        self.stack=[]
    
    def push(self, item):

        self.stack.append(item)
    
    def is_empty(self):

        return self.stack==[]

    def pop(self):
        
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()
    
    def peek(self):

        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    