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
        self.initialize()

    def initialize(self):
        self.bank0 = [[0] * 8] * 128  
        self.bank1 = [[0] * 8] * 128
        self.WREG = 0
        self.pCounter = 0
        
        self.initBank0()
        self.initBank1()

        self.memory = [None] * 2

        self.memory[0] = self.bank0
        self.memory[1] = self.bank1

    def initBank0(self):
        # initialize Bank 0
        # TMR0 is unknown
        self.bank0[0x01] = [0] * 8

        # STATUS
        self.bank0[0x03] = [0, 0, 0, 1, 1, 0, 0, 0]

        # FSR
        self.bank0[0x04] = [0] * 8

        # PORTA
        self.bank0[0x05] = [0, 0, 0, 0, 0, 0, 0, 0]

        # PORTB
        self.bank0[0x06] = [0] * 8

        # EEDATA
        self.bank0[0x08] = [0] * 8

        # EEADR
        self.bank0[0x09] = [0] * 8

        # PCLATH
        self.bank0[0x0A] = [0] * 8

        # INTCON
        self.bank0[0x0B] = [0, 0, 0, 0, 0, 0, 0, 0]

    def initBank1(self):


        # OPTION_REG
        self.bank1[0x01] = [1] * 8

        # STATUS
        self.bank1[0x03] = [0, 0, 0, 1, 1, 0, 0, 0]

        # FSR
        self.bank1[0x04] = [0] * 8

        # TRISA
        self.bank1[0x05] = [0, 0, 0, 1, 1, 1, 1, 1]

        # TRISB
        self.bank1[0x06] = [1] * 8

        # EECON1
        self.bank1[0x08] = [0, 0, 0, 0, 0, 0, 0, 0]

        # INTCON
        self.bank1[0x0B] = [0, 0, 0, 0, 0, 0, 0, 0]

    def getActiveBank(self):
        return self.memory[0][0x03][7-5]  # STATUS register, bit 5 (RP0) indicates active bank

    def getW(self) -> int:
        return self.WREG
    
    def getPCL(self) -> int:
        return self.readRegister(0x02, 1)
    
    def setPCL(self, value: int) -> None:
        self.writeRegister(0x02, value)

    def incPCL(self) -> None:
        newVal = self.readRegister(0x02, 1) + 1
        if newVal >= 256:
            newVal = 0
            self.incPCLATH()
        # self.bank0[0x02] = newVal
        # self.bank1[0x02] = newVal
        self.setPCL(newVal)

    def getPCLATH(self) -> int:
        return self.readRegister(0x0A, 1)
    
    def setPCLATH(self, value: int) -> None:
        self.writeRegister(0x0A, value, 1)

    def incPCLATH(self) -> None:
        newVal = self.getPCLATH()
        if (newVal & 0x07) == 7:
            newVal = newVal & 0x18
        else:
            newVal += 1
        self.setPCLATH(newVal)

    def setPCounter(self, value=None) -> None:
        if value != None:
            self.pCounter = value
        else:
            self.pCounter = (self.getPCLATH() << 8) + self.getPCL()

    def getPCounter(self) -> int:
        return self.pCounter
    
    def resetPC(self) -> None:
        self.setPCounter(0)
        self.setPCL(0)
        self.setPCLATH(0)
    
    def readRegister(self, register: int, bank=None) -> int:
        if register == 'w':
            return self.WREG
        elif register in range(0x00, 0x80):
            if register == 0:
                register = self.readRegister(4)
            bank = self.getActiveBank() if bank == None else bank
            return int(("".join([str(x) for x in self.memory[bank][register]])),2)
            # return int(self.memory[self.getActiveBank()][register],2)
        else:
            raise ValueError("Invalid register address")

    def writeRegister(self, register: int, value: int, bank=None) -> None:
        if register == 'w':
            self.WREG = value
        elif register in range(0x00, 0x80):
            test = bin(value)[2:]
            if register == 0:
                register = self.readRegister(4)
            string = ('0'*(8-len(test))) + test
            activeReg = self.getActiveBank() if bank == None else bank
            if register in MIRRORED_REGISTERS:
                self.memory[1 - activeReg][register] = [int(char) for char in string]
            self.memory[activeReg][register] = [int(char) for char in string]
        else:
            raise ValueError("Invalid register address")
        
    def setBit(self, register: int, bit: int, value: int) -> None:
        if register in range(0x00, 0x80):
            if register == 0:
                register = self.readRegister(4)
            if register in MIRRORED_REGISTERS:
                self.memory[1 - self.getActiveBank()][register][7-bit] = value
            self.memory[self.getActiveBank()][register][7-bit] = value
        else:
            raise ValueError("Invalid register address")
        
    def getBit(self, register: int, bit: int) -> int:
        if register in range(0x00, 0x80):
            if register == 0:
                register = self.readRegister(4)
            return self.memory[self.getActiveBank()][register][7-bit]
        else:
            raise ValueError("Invalid register address")

    def getPrescaler(self):
        scaler = ("".join([str(x) for x in self.memory[1][0x01]]))
        test:int = (int(scaler, 2) & 0x07)
        if int(scaler[4]) == 0: 
            test +=1
        test = 2**(test)
        return (int(scaler[2]), int(scaler[4]), test)
    
    def incTimer0(self):
        value = int(("".join([str(x) for x in self.memory[0][1]])),2)
        test = bin((value+1) & 0xFF)[2:]
        string = ('0'*(8-len(test))) + test
        self.memory[0][1] = [int(char) for char in string]


class ProgramMemory:
    def __init__(self):
        self.memory = []

    def write(self, value):
        self.memory = value

    def read(self, address=None):
        if address == None: return self.memory
        if address < 0 or address >= len(self.memory):
            raise ValueError("Address out of range")
        return self.memory[address]
    
    def reset(self):
        self.memory = []




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
    
    def get(self):
        return self.stack.copy()
    