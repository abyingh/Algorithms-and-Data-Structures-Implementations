""" A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, 
together with next pointer and data which are there in singly linked list. """



class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getSize(self):
        temp = self.head
        i = 1
        while temp.next:
            i += 1
            temp = temp.next
        return i

    def insertHead(self, item):
        new = Node(item)
        if self.head is not None:
            self.head.prev = new
            new.next = self.head
        else:
            self.tail = new

        self.head = new

    def insertTail(self, item):
        new = Node(item)
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
            self.tail = new
            new.prev = temp
            temp.next = new
        else:
            self.head = new
            self.tail = new

    def insertIndex(self, item, index):
        if 0 < index < self.getSize():
            new = Node(item)
            temp = self.head
            for i in range(index):
                temp = temp.next

            prev = temp.prev
            prev.next = new
            temp.prev = new
            new.next = temp
            new.prev = prev
            temp = None

        else: IndexError('Index is out of range!')

    def remove(self, item):
        if item in self.linkedList() and self.head:
            temp = self.head
            while temp.value != item:
                temp = temp.next
            
            prev = temp.prev
            next = temp.next
            next.prev = prev
            prev.next = next
            temp = None
            
    def linkedList(self):
        temp = self.head
        l = []
        while temp:
            l.append(temp.value)
            temp = temp.next
        return l
