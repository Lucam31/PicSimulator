# if memory is unknown on power-on reset, the value will be None

MIRRORED_REGISTERS = {
    0x02,     # PCL
    0x03,  # STATUS
    0x04,     # FSR
    0x0A,  # PCLATH
    0x0B   # INTCON
}

class DataMemory:
    def __init__(self):
        self.bank0 = [[0] * 8] * 128  
        self.bank1 = [[0] * 8] * 128
        self.WREG = [0] * 8  
        
        self.initBank0()
        self.initBank1()

        self.memory = [None] * 2

        self.memory[0] = self.bank0
        self.memory[1] = self.bank1

    def initBank0(self):
        # initialize Bank 0
        # TMR0 is unknown
        self.bank0[0x01] = [None] * 8

        # STATUS
        self.bank0[0x03] = [None, None, None, 1, 1, 0, 0, 0]

        # FSR
        self.bank0[0x04] = [None] * 8

        # PORTA
        self.bank0[0x05] = [None, None, None, None, None, 0, 0, 0]

        # PORTB
        self.bank0[0x06] = [None] * 8

        # EEDATA
        self.bank0[0x08] = [None] * 8

        # EEADR
        self.bank0[0x09] = [None] * 8

        # PCLATH
        self.bank0[0x0A] = [0] * 8

        # INTCON
        self.bank0[0x0B] = [None, 0, 0, 0, 0, 0, 0, 0]

    def initBank1(self):


        # OPTION_REG
        self.bank1[0x01] = [1] * 8

        # STATUS
        self.bank1[0x03] = [None, None, None, 1, 1, 0, 0, 0]

        # FSR
        self.bank1[0x04] = [None] * 8

        # TRISA
        self.bank1[0x05] = [1, 1, 1, 1, 1,0, 0, 0]

        # TRISB
        self.bank1[0x06] = [1] * 8

        # EECON1
        self.bank1[0x08] = [0, 0, 0, None, 0, 0, 0, 0]

        # INTCON
        self.bank1[0x0B] = [None, 0, 0, 0, 0, 0, 0, 0]

    def getActiveBank(self):
        return self.memory[0][0x03][5]  # STATUS register, bit 5 (RP0) indicates active bank

    def getW(self):
        return self.WREG
    
    def getPCL(self):
        return self.bank1[0x02]
    
    def setPCL(self, value):
        self.writeRegister(0x02, value)
    
    def readRegister(self, register):
        if register == 'w':
            return self.WREG
        elif register in range(0x00, 0x80):
            return self.memory[self.getActiveBank()][register]
        else:
            raise ValueError("Invalid register address")

    def writeRegister(self, register, value):
        if register == 'w':
            self.WREG = value
        elif register in range(0x00, 0x80):
            if register in MIRRORED_REGISTERS:
                self.memory[1 - self.getActiveBank()][register] = value
            self.memory[self.getActiveBank()][register] = value
        else:
            raise ValueError("Invalid register address")
        
    def setBit(self, register, bit, value):
        if register == 'w':
            self.WREG[bit] = value
        elif register in range(0x00, 0x80):
            if register in MIRRORED_REGISTERS:
                self.memory[1 - self.getActiveBank()][register][bit] = value
            self.memory[self.getActiveBank()][register][bit] = value
        else:
            raise ValueError("Invalid register address")
        
    def getBit(self, register, bit):
        if register == 'w':
            return self.WREG[bit]
        elif register in range(0x00, 0x80):
            return self.memory[self.getActiveBank()][register][bit]
        else:
            raise ValueError("Invalid register address")

    def getActiveBank(self):
        return self.memory[0][0x03][5]  # STATUS register, bit 5 (RP0) indicates active bank

    def getW(self):
        return self.WREG
    
    def getPCL(self):
        return self.bank1[0x02]
    
    def setPCL(self, value):
        self.writeRegister(0x02, value)
    
    def readRegister(self, register):
        if register == 'w':
            return self.WREG
        elif register in range(0x00, 0x80):
            return self.memory[self.getActiveBank()][register]
        else:
            raise ValueError("Invalid register address")

    def writeRegister(self, register, value):
        if register == 'w':
            self.WREG = value
        elif register in range(0x00, 0x80):
            if register in MIRRORED_REGISTERS:
                self.memory[1 - self.getActiveBank()][register] = value
            self.memory[self.getActiveBank()][register] = value
        else:
            raise ValueError("Invalid register address")
        
    def setBit(self, register, bit, value):
        if register == 'w':
            self.WREG[bit] = value
        elif register in range(0x00, 0x80):
            if register in MIRRORED_REGISTERS:
                self.memory[1 - self.getActiveBank()][register][bit] = value
            self.memory[self.getActiveBank()][register][bit] = value
        else:
            raise ValueError("Invalid register address")
        
    def getBit(self, register, bit):
        if register == 'w':
            return self.WREG[bit]
        elif register in range(0x00, 0x80):
            return self.memory[self.getActiveBank()][register][bit]
        else:
            raise ValueError("Invalid register address")

class ProgramMemory:
    def __init__(self, size=1024):
        self.size = size
        self.memory = [0] * size

    def write(self, value):
        self.memory = value

    def read(self, address=None):
        if address == None: return self.memory
        if address < 0 or address >= len(self.memory):
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
    