class ProgramMemory:
    def __init__(self, size=1024):
        self.size = size
        self.memory = [0] * size

    def write(self, address, value):
        if address < 0 or address >= self.size:
            raise ValueError("Address out of range")
        self.memory[address] = value

    def read(self, address):
        if address < 0 or address >= self.size:
            raise ValueError("Address out of range")
        return self.memory[address]

    def reset(self):
        self.memory = [0] * self.size



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
