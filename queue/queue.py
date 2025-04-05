class Stack:
  def __init__(self):
    self.stack = []
  def push(self, el):
    self.stack.append(el)
  def pop(self):
    return self.stack.pop()
  def peek(self):
    return self.stack[-1]
  def size(self):
    return len(self.stack)
  def is_empty(self):
    return len(self.stack) == 0
class MyQueue:

  def __init__(self):
    self.stack = Stack()

  def push(self, x: int) -> None:
    self.stack.push(x)

  def pop(self) -> int:
    temp = Stack()
    while not self.stack.is_empty():
      temp.push(self.stack.pop())
    el = temp.pop()
    while not temp.is_empty():
      self.stack.push(temp.pop())
    return el
  def peek(self) -> int:
    temp = Stack()
    while not self.stack.is_empty():
      temp.push(self.stack.pop())
    el = temp.peek()
    while not temp.is_empty():
      self.stack.push(temp.pop())
    return el
      

  def empty(self) -> bool:
    return self.stack.is_empty()