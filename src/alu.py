
class ALU:
    def __init__(self, memory):
        self.memory = memory

    def execute(self, command):
        operation, reg_num, dest_bit = command

        if operation == "addwf":
            self.add(dest_bit, reg_num)
        elif operation == "subwf":
            self.sub(dest_bit, reg_num)
        elif operation == "andwf":
            self.bitwise_and(dest_bit, reg_num)
        elif operation == "iorwf":
            self.bitwise_or(dest_bit, reg_num)
        elif operation == "xorwf":
            self.bitwise_xor(dest_bit, reg_num)

        elif operation == "addlw":
            self.add(dest_bit, None, reg_num)
        elif operation == "sublw":
            self.sub(dest_bit, None, reg_num)
        elif operation == "andlw":
            self.bitwise_and(dest_bit, None, reg_num)
        elif operation == "iorlw":
            self.bitwise_or(dest_bit, None, reg_num)
        elif operation == "xorlw":
            self.bitwise_xor(dest_bit, None, reg_num)
        else:
            raise ValueError(f"Unknown operation: {operation}")

    def add(self, dest, reg_num, value=None):
        if(reg_num != None):
            result = self.memory.readRegister(reg_num) + self.memory.getW()
        else:
            result = value + self.memory.getW()
            
        self.memory.writeRegister(reg_num if dest else 'w', result & 0xFF)  # Simulate 8-bit overflow

    def sub(self, dest, reg_num, value=None):
        if(reg_num != None):
            result = self.memory.readRegister(reg_num) - self.memory.getW()
        else:
            result = value - self.memory.getW()

        self.memory.writeRegister(reg_num if dest else 'w', result & 0xFF)  # Simulate 8-bit overflow

    def bitwise_and(self, dest, reg_num, value=None):
        if(reg_num != None):
            result = self.memory.readRegister(reg_num) & self.memory.getW()
        else:
            result = value & self.memory.getW()

        self.memory.writeRegister(reg_num if dest else 'w', result & 0xFF)  # Simulate 8-bit overflow

    def bitwise_or(self, dest, reg_num, value=None):
        if(reg_num != None):
            result = self.memory.readRegister(reg_num) | self.memory.getW()
        else:
            result = value | self.memory.getW()

        self.memory.writeRegister(reg_num if dest else 'w', result & 0xFF)  # Simulate 8-bit overflow

    def bitwise_xor(self, dest, reg_num, value=None):
        if(reg_num != None):
            result = self.memory.readRegister(reg_num) ^ self.memory.getW()
        else:
            result = value ^ self.memory.getW()

        self.memory.writeRegister(reg_num if dest else 'w', result & 0xFF)  # Simulate 8-bit overflow