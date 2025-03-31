

class Stack:
    def __init__(self, size=8):
        self.size = size
        self.stack = []
    
    def push(self, value):
        if len(self.stack) >= self.size:
            # raise OverflowError("Stack overflow")
            self.stack.pop(0)
            self.stack.append(value)
            #
        self.stack.append(value)
    
    def pop(self):
        if not self.stack:
            raise IndexError("Stack underflow")
        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
