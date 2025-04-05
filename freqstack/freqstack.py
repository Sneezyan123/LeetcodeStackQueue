from collections import deque

class FreqStack:

    def __init__(self):
        self.stack = deque()
        self.dct = {}
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val not in self.dct:
            self.dct[val] = 1
        else:
            self.dct[val] += 1