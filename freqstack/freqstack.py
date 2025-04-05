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
    def pop(self) -> int:
        max_freq = max(self.dct.values())
        
        temp = deque()
        popped_val = -1
        while self.stack:
            popped_val = self.stack.pop()
            if self.dct[popped_val] != max_freq:
                temp.appendleft(popped_val)
            else:
                self.dct[popped_val] -= 1
                break

        self.stack.extend(temp)
        return popped_val
