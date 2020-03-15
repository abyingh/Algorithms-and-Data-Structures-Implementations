""" A stack is a linear data structure which follows a particular order in which the operations are performed.
The order is last in first out(LIFO). 
3 operations: push, pop, top(peak)
"""


class Stack:
    def __init__(self):
        self.items = []
        self.head = None
        self.tail = None

    def getSize(self):
        return len(self.items)

    def isEmpty(self):
        return 'YES' if self.getSize() == 0 else 'NO'
        
    def push(self, item):
        if len(self.items) == 0:
            self.head = item
            self.tail = item
        else:
            self.head = item

        self.items.insert(0, item)

    def pop(self, idx):
        self.items.pop(idx)
        self.head = data[0]

    def top(self):
        return self.items[-1]
