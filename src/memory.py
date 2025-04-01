# if memory is unknown on power-on reset, the value will be None


class Memory:
    def __init__(self):
        self.bank0 = [[0] * 8] * 128  
        self.bank1 = [[0] * 8] * 128  
        
        self.initBank0()
        self.initBank1()

        self.memory = []

        self.memory[0] = self.bank0
        self.memory[1] = self.bank1     

    def initBank0(self):
        # initialize Bank 0
        # TMR0 is unknown
        self.bank0[0x01] = [None] * 8

        # STATUS
        self.bank0[0x03] = [0, 0, 0, 1, 1, None, None, None]

        # FSR
        self.bank0[0x04] = [None] * 8

        # PORTA
        self.bank0[0x05] = [0, 0, 0, None, None, None, None, None]

        # PORTB
        self.bank0[0x06] = [None] * 8

        # EEDATA
        self.bank0[0x08] = [None] * 8

        # EEADR
        self.bank0[0x09] = [None] * 8

        # PCLATH
        self.bank0[0x0A] = [0] * 8

        # INTCON
        self.bank0[0x0B] = [0, 0, 0, 0, 0, 0, 0, None]

    def initBank1(self):
        # OPTION_REG
        self.bank1[0x01] = [1] * 8

        # STATUS
        self.bank1[0x03] = [0, 0, 0, 1, 1, None, None, None]

        # FSR
        self.bank1[0x04] = [None] * 8

        # TRISA
        self.bank1[0x05] = [0, 0, 0, 1, 1, 1, 1, 1]

        # TRISB
        self.bank1[0x06] = [1] * 8

        # EECON1
        self.bank1[0x08] = [0, 0, 0, 0, None, 0, 0, 0]

        # INTCON
        self.bank1[0x0B] = [0, 0, 0, 0, 0, 0, 0, None]

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
        self.maxSize = size
        self.stack = []
    
    def push(self, value):
        if len(self.stack) >= self.maxSize:
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
