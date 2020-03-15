""" Deque is a generalized version of Queue data structure that allows insert and delete at both ends. """


class Deque:
    def __init__(self):
        self.items = []

    def getSize(self):
        return len(self.items)

    def isEmpty(self):
        return 'YES' if self.getSize() == 0 else 'NO'

    def addFront(self, item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)
