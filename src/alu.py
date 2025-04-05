
class ALU:
    def __init__(self, memory):
        self.memory = memory

    def execute(self, command):
        operation, reg_num, dest_bit = command

        if operation == "addwf":
            self.add(dest_bit, reg_num)
        elif operation == "subwf":
            self.subwf(dest_bit, reg_num)
        elif operation == "andwf":
            self.bitwise_and(dest_bit, reg_num)
        elif operation == "iorwf":
            self.bitwise_or(dest_bit, reg_num)
        elif operation == "xorwf":
            self.bitwise_xor(dest_bit, reg_num)

        elif operation == "addlw":
            self.add(dest_bit, 'w', reg_num)
        elif operation == "sublw":
            self.sub(dest_bit, 'w', reg_num)
        elif operation == "andlw":
            self.bitwise_and(dest_bit, 'w', reg_num)
        elif operation == "iorlw":
            self.bitwise_or(dest_bit, 'w', reg_num)
        elif operation == "xorlw":
            self.bitwise_xor(dest_bit, 'w', reg_num)
        else:
            raise ValueError(f"Unknown operation: {operation}")

    def add(self, dest, reg_num, value=None):
        if(reg_num != 'w'):
            value = self.memory.readRegister(reg_num)
        result = self.memory.getW() + value
        self.memory.setBit(0x03, 0, 1 if result >= 256 else 0)
        result = int(int(bin(result),2) & int('0b11111111',2))
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)
            
        self.memory.writeRegister(reg_num if dest else 'w', result)  # Simulate 8-bit overflow
        # print(value)
        # print(self.memory.getW())
        # print(self.memory.readRegister(reg_num))

    def sub(self, dest, reg_num, value=None):
        if(reg_num != 'w'):
            value = self.memory.readRegister(reg_num)
        result = self.memory.getW() - value
        if result < 0:
            result = (result * (-1)-1) ^ 0xFF
        self.memory.setBit(0x03, 0, 0 if result < 0 else 1)
        result = int(int(bin(result),2) & int('0b11111111',2))
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)

        self.memory.writeRegister(reg_num if dest else 'w', result)  # Simulate 8-bit overflow
    
    def subwf(self, dest, reg_num):
        value = self.memory.readRegister(reg_num)
        result = value - self.memory.getW()
        if result < 0:
            result = (result * (-1)-1) ^ 0xFF
        self.memory.setBit(0x03, 0, 0 if result < 0 else 1)
        result = int(int(bin(result),2) & int('0b11111111',2))
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)

        self.memory.writeRegister(reg_num if dest else 'w', result)  # Simulate 8-bit overflow

    def bitwise_and(self, dest, reg_num, value=None):
        if(reg_num != 'w'):
            value = self.memory.readRegister(reg_num)
        result = self.memory.getW() & value
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)
        result = int(bin(result),2)

        self.memory.writeRegister(reg_num if dest else 'w', result)  # Simulate 8-bit overflow

    def bitwise_or(self, dest, reg_num, value=None):
        if(reg_num != 'w'):
            value = self.memory.readRegister(reg_num)
        result = self.memory.getW() | value
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)
        result = int(bin(result),2)

        self.memory.writeRegister(reg_num if dest else 'w', result)  # Simulate 8-bit overflow

    def bitwise_xor(self, dest, reg_num, value=None):
        if(reg_num != 'w'):
            value = self.memory.readRegister(reg_num)
        result = self.memory.getW() ^ value
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)
        result = int(bin(result),2)

        self.memory.writeRegister(reg_num if dest else 'w', result)  # Simulate 8-bit overflow

    def addWithoutW(self, val1, val2):
        result = val1 + val2
        self.memory.setBit(0x03, 0, 1 if result >= 256 else 0)
        result = int(int(bin(result),2) & int('0b11111111',2))
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)
        return result
    
    def subWithoutW(self, val1, val2):
        result = val1 - val2
        if result < 0:
            result = (result * (-1)-1) ^ 0xFF
        self.memory.setBit(0x03, 0, 0 if result < 0 else 1)
        result = int(int(bin(result),2) & int('0b11111111',2))
        self.memory.setBit(0x03, 2, 1 if result == 0 else 0)
        return result
    
    def incTimer(self, additional=False):
        # inc timer (01h)
        pass