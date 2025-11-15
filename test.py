from src.Stack import Stack
from src.Queue import Queue

q=Queue()
print(q.isEmpty())
q.enqueue(4)
print(q.list)
q.enqueue("dog")
print(q.size())
print(q.isEmpty())
print(q.dequeue())
print(q.size())