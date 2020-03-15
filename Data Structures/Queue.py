"""A Queue is a linear structure which follows a particular order in which the operations are performed. 
The order is first in first out (FIFO).
3 operations: enqueue, dequeue, peek
"""


class Queue:
    def __init__(self):
        self.items = []
        self.head = None
        self.tail = None

    def getSize(self):
        return len(self.items)

    def isEmpty(self):
        return 'YES' if self.getSize() == 0 else 'NO'

    def enqueue(self,item):
        self.items.append(item)
        if self.getSize() == 1:
            self.head = item
            self.tail = item
        else:
            self.tail = item

    def dequeue(self):
        self.items.pop(0)
        if self.getSize() != 0:
            self.head = self.items[0]
        else:
            self.head = None
            self.tail = None
    
    def peek(self):
        return self.head
