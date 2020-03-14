""" A dynamic array automatically grows when we try to make an insertion. If its capacity will be exceeded with a new 
insertion, its capacity is doubled for space every time.
"""


import ctypes

class Array:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __sizeof__(self):
        return self.n

    def __getitem__(self, item):
        if 0 <= item < self.n:
            return self.A[item]
        else:
            return IndexError('Index is out of range!')

    def append(self, item):
        if  self.n >= self.capacity:
            self.resize(self.capacity*2)
        self.A[self.n] = item
        self.n += 1

    def resize(self, capacity):
        B = self.make_array(capacity)
        for idx, i in enumerate(self.A):
            B[idx] = self.A[idx]
        self.A = B
        self.capacity = capacity

    def remove(self, item):
        if self.n - 1 == int(self.capacity / 2):
            cap = int(self.capacity / 2)
            C = self.make_array(cap)
        else:
            cap = int(self.capacity)
            C = self.make_array(int(self.capacity))

        for idx,i in enumerate(self.A):
            index = 0
            if i != item:
                C[index] = self.A[idx]
                print(C[index], self.A[idx], cap)
                index += 1
                if cap == index:
                    break

        self.A = C
        self.resize(cap)
        self.n -= 1

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()
