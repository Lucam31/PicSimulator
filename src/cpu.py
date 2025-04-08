from memory import ProgramMemory, DataMemory, Stack
from decode import Decoder
from fileReader import FileReader
from alu import ALU
import os

class CPU:
    def __init__(self, gui=None):
        self.gui = gui
        self.pMemory = ProgramMemory()
        self.dMemory = DataMemory()
        self.stack = Stack()
        self.decoder = Decoder()
        self.fileReader = FileReader(self.pMemory)
        self.alu = ALU(self.dMemory)
        self.program_file = os.getcwd() + "/Testprogramme/TPicSim7.LST"
        self.ready = False
        

    def load_program(self, path=None):
        self.fileReader.readFile(self.program_file if path == None else path)
        self.ready = True

    def execute(self):
        if not self.ready: return
        self.timer = 0
        while(1):
            cmd = self.pMemory.read(self.dMemory.getPCL())
            inst = self.decoder.decode('0x'+str(cmd))
            print(inst)
            # self.dMemory.setPCL(self.dMemory.getPCL()+1)
            self.dMemory.incPCL()
            if self.dMemory.getPCL() == len(self.pMemory.memory): 
                break
            if 'add' in inst[0] or 'sub' in inst[0] or 'and' in inst[0] or 'ior' in inst[0] or 'xor' in inst[0]:
                self.alu.execute(inst)
                # continue
                #print("ALU called")
            match inst[0]:
                case 'movlw':
                    self.dMemory.writeRegister('w', inst[1])
                case 'movwf':
                    self.dMemory.writeRegister(inst[1], self.dMemory.getW())
                case 'movf':
                    val = self.dMemory.readRegister(inst[1])
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val)
                    self.dMemory.setBit(0x03, 2, 1 if val == 0 else 0)
                case 'goto':
                    if self.dMemory.getPCL() == inst[1]: break
                    self.dMemory.setPCL(inst[1])
                case 'sleep':
                    self.timer += 1#inst[1]
                    # fehlt noch was
                case 'call':
                    self.stack.push(self.dMemory.getPCL()+1)
                    self.dMemory.setPCL(inst[1])
                case 'ret':
                    self.dMemory.setPCL(self.stack.pop())
                case 'nop':
                    pass
                case 'retlw':
                    self.dMemory.writeRegister('w', inst[1])
                    self.dMemory.setPCL(self.stack.pop())
                case 'clrf':
                    self.dMemory.writeRegister(inst[1], 0)
                case 'clrw':
                    self.dMemory.writeRegister('w', 0)
                case 'incf':
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', self.alu.addWithoutW(self.dMemory.readRegister(inst[1]), 1))
                case 'incfsz':
                    val = self.alu.addWithoutW(self.dMemory.readRegister(inst[1]), 1)
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val)
                    if val == 0: self.dMemory.incPCL()
                case 'decf':
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', self.alu.subWithoutW(self.dMemory.readRegister(inst[1]), 1))
                case 'decfsz':
                    val = self.alu.subWithoutW(self.dMemory.readRegister(inst[1]), 1)
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val)
                    if val == 0: self.dMemory.incPCL()
                case 'swapf':
                    keep = bin(self.dMemory.readRegister(inst[1]))[2:]
                    keep = '0'*(8-len(keep)) + keep
                    low = keep[4:8]
                    high = keep[0:4]
                    new = int('0b' + low + high,2)
                    self.dMemory.writeRegister(inst[1], new)
                case 'comf':
                    val = self.dMemory.readRegister(inst[1]) ^ 0xFF
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val)
                case 'rlf':
                    val = self.dMemory.readRegister(inst[1])
                    val = val << 1
                    val += self.dMemory.getBit(0x03, 0)
                    self.dMemory.setBit(0x03, 0, 1 if val >= 256 else 0)
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val & 0xFF)
                case 'rrf':
                    val = self.dMemory.readRegister(inst[1])
                    cSet = self.dMemory.getBit(0x03, 0)
                    self.dMemory.setBit(0x03, 0, 1 if str(val)[-1] == '1' else 0)
                    val = val >> 1
                    val += 128*cSet
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val & 0xFF)
                case 'bcf':
                    self.dMemory.setBit(inst[1], inst[2], 0)
                case 'bsf':
                    self.dMemory.setBit(inst[1], inst[2], 1)
                case 'btfsc':
                    if not self.dMemory.getBit(inst[1], inst[2]): self.dMemory.incPCL()
                case 'btfss':
                    if self.dMemory.getBit(inst[1], inst[2]): self.dMemory.incPCL()
                # clrwdt, retfie
            # self.dMemory.writeRegister(0x01, int(self.timer/4))
            print("W: " + hex(self.dMemory.getW()))
            print("Wert1: " + hex(self.dMemory.readRegister(12)))
            print("Wert2: " + hex(self.dMemory.readRegister(13)))
            # print("FSR: " + hex(self.dMemory.readRegister(4)))
            print("")
            self.gui.updateUI()

        keep = self.dMemory.getW()
        print("W: " + hex(keep))
        print("Wert1: " + hex(self.dMemory.readRegister(0x0C)))
        print("Wert2: " + hex(self.dMemory.readRegister(0x0D)))
        # print("FSR: " + hex(self.dMemory.readRegister(4)))
        print("Program done!")

    def getMemInHex(self):
        hexMem = self.dMemory.memory[0] + self.dMemory.memory[1]
        for i in range(len(hexMem)):
            string = ("".join([str(x) for x in hexMem[i]]))
            hexMem[i] = int(string, 2)
        return hexMem
    
    def getFile(self):
        return self.fileReader.getFile()


if __name__ == "__main__":
    test = CPU()
    # test.load_program()
    # test.execute()
    print(test.getMemInHex())