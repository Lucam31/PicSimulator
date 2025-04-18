from memory import ProgramMemory, DataMemory, Stack
from decode import Decoder
from fileReader import FileReader
from alu import ALU
import os
from time import sleep

from PySide6.QtCore import QObject, Signal, QThread, Slot

class CPU(QThread):
    update_signal = Signal(int)  # Signal to notify the GUI to update
    finished_signal = Signal()  # Signal to notify when execution is complete

    def __init__(self, gui=False):
        super().__init__()
        self.guiSet = gui
        self.pMemory = ProgramMemory()
        self.dMemory = DataMemory()
        self.stack = Stack()
        self.decoder = Decoder()
        self.fileReader = FileReader(self.pMemory)
        self.alu = ALU(self.dMemory)
        self.program_file = os.getcwd() + "/Testprogramme/TPicSim2.LST"
        self.ready = False
        self.stopThread = False
        self.pauseThread = True if gui else False
        self.clock, self.timer, self.flankeVal, self.flankeClock = 0, 0, 0, 0
        self.stepInVar, self.stepOverVar = False, False
        self.flanke = False
        self.t0cs, self.psa, self.scaling = 1, 1, 16
        self.lastPC = 0
        # self.initialUpdate = True
        

    def load_program(self, path=None):
        keep = self.fileReader.readFile(self.program_file if path == None else path)
        self.ready = True
        return keep

    def execute(self):
        if not self.ready: 
            return
        while(1):
            # check for interrupts
            intcon = self.dMemory.readRegister(0x0B)
            if(intcon & 0x80 > 0): #if GIE is set, ints are enabled
                if(intcon & 0x38 > 0):
                    if(intcon & 0x07 > 0): 
                        self.dMemory.setBit(0x0B, 7, 0)
                        self.stack.push(self.dMemory.getPCounter())
                        self.dMemory.setPCL(4)
                        self.dMemory.setPCLATH(0)
                        self.dMemory.setPCounter(4)
                        self.clock += 2
                        self.timer += 2

            while(self.pauseThread):
                if(self.stopThread): break
                if self.stepInVar or self.stepOverVar: 
                    self.stepOverVar = False
                    self.stepInVar = False
                    break
            if(self.stopThread): 
                break
            cmd = self.pMemory.read(self.dMemory.getPCounter())
            inst = self.decoder.decode('0x'+str(cmd))
            print(inst)
            self.lastPC = self.dMemory.getPCounter()
            self.dMemory.incPCL()
            # self.dMemory.incPCounter()
            if 'add' in inst[0] or 'sub' in inst[0] or 'and' in inst[0] or 'ior' in inst[0] or 'xor' in inst[0]:
                self.alu.execute(inst)
            match inst[0]:
                case 'movlw':
                    self.dMemory.writeRegister('w', inst[1])
                case 'movwf':
                    self.dMemory.writeRegister(inst[1], self.dMemory.getW())
                    if inst[1] == 1: self.timer = 0
                case 'movf':
                    val = self.dMemory.readRegister(inst[1])
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val)
                    self.dMemory.setBit(0x03, 2, 1 if val == 0 else 0)
                case 'goto':
                    pclath = int(("".join([str(x) for x in self.dMemory.memory[1][0x0A]])[3:5]),2) << 3
                    val = bin(inst[1])[2:]
                    # val = '0'*(11-len(val)) + val
                    pc = (pclath << 8) + int(val,2)
                    self.dMemory.setPCounter(pc)
                    self.dMemory.setPCL(self.dMemory.getPCounter() & 0xFF)
                    self.clock += 1
                    self.timer += 1
                case 'sleep':
                    self.clock += 1#inst[1]
                    self.timer += 1
                    # fehlt noch was
                case 'call':
                    self.stack.push(self.dMemory.getPCounter())
                    pclath = int(("".join([str(x) for x in self.dMemory.memory[1][0x0A]])[3:5]),2) << 3
                    val = bin(inst[1])[2:]
                    # val = '0'*(11-len(val)) + val
                    pc = (pclath << 8) + int(val,2)
                    self.dMemory.setPCounter(pc)
                    self.dMemory.setPCL(self.dMemory.getPCounter() & 0xFF)
                    self.clock += 1
                    self.timer += 1
                case 'ret':
                    self.dMemory.setPCounter(self.stack.pop())
                    self.dMemory.setPCL(self.dMemory.getPCounter() & 0xFF)
                    self.clock += 1
                    self.timer += 1
                case 'nop':
                    pass
                case 'retlw':
                    self.dMemory.writeRegister('w', inst[1])
                    self.dMemory.setPCounter(self.stack.pop())
                    self.dMemory.setPCL(self.dMemory.getPCounter() & 0xFF)
                    self.clock += 1
                    self.timer += 1
                case 'retfie':
                    self.dMemory.setBit(0x0B, 7, 1)
                    self.dMemory.setPCounter(self.stack.pop())
                    self.dMemory.setPCL(self.dMemory.getPCounter() & 0xFF)
                    self.clock += 1
                    self.timer += 1
                    # implementation missing
                case 'clrf':
                    self.dMemory.writeRegister(inst[1], 0)
                case 'clrw':
                    self.dMemory.writeRegister('w', 0)
                case 'incf':
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', self.alu.addWithoutW(self.dMemory.readRegister(inst[1]), 1))
                case 'incfsz':
                    val = self.alu.addWithoutW(self.dMemory.readRegister(inst[1]), 1)
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val)
                    if val == 0: 
                        self.dMemory.incPCL()
                        # self.dMemory.incPCounter()
                        self.clock += 1
                        self.timer += 1
                case 'decf':
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', self.alu.subWithoutW(self.dMemory.readRegister(inst[1]), 1))
                case 'decfsz':
                    val = self.alu.subWithoutW(self.dMemory.readRegister(inst[1]), 1)
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val)
                    if val == 0: 
                        self.dMemory.incPCL()
                        # self.dMemory.incPCounter()
                        self.clock += 1
                        self.timer += 1
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
                    self.dMemory.setBit(0x03, 0, 1 if str(bin(val))[-1] == '1' else 0)
                    val = val >> 1
                    if cSet: 
                        val = val | 0x80
                    self.dMemory.writeRegister(inst[1] if inst[2] else 'w', val & 0xFF)
                case 'bcf':
                    self.dMemory.setBit(inst[1], inst[2], 0)
                case 'bsf':
                    self.dMemory.setBit(inst[1], inst[2], 1)
                case 'btfsc':
                    if not self.dMemory.getBit(inst[1], inst[2]): 
                        self.dMemory.incPCL()
                        # self.dMemory.incPCounter()
                        self.clock += 1
                        self.timer += 1
                case 'btfss':
                    if self.dMemory.getBit(inst[1], inst[2]): 
                        self.dMemory.incPCL()
                        # self.dMemory.incPCounter()
                        self.clock += 1
                        self.timer += 1
                # clrwdt, retfie
            if self.dMemory.getPCounter() == len(self.pMemory.memory):
                break
            # increase timer and counter
            self.clock += 1
            self.timer += 1
            self.t0cs, self.psa, self.scaling = self.dMemory.getPrescaler()
            if not self.t0cs and not self.psa:
                try:
                    if self.clock % self.scaling == 0:
                        self.dMemory.incTimer0()
                except: pass

            print("W: " + hex(self.dMemory.getW()))
            # print("Wert1: " + hex(self.dMemory.readRegister(12)))
            # print("Wert2: " + hex(self.dMemory.readRegister(13)))
            # print("FSR: " + hex(self.dMemory.readRegister(4)))
            print("")
            if self.guiSet: self.updateUI()
            # QThread.sleep(0.05)
            sleep(0.05)

        keep = self.dMemory.getW()
        print("W: " + hex(keep))
        # print("Wert1: " + hex(self.dMemory.readRegister(0x0C)))
        # print("Wert2: " + hex(self.dMemory.readRegister(0x0D)))
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
    
    def reset(self):
        self.clock = 0
        self.dMemory.initialize()
        self.stack.stack = []
        self.pauseThread = True
        self.dMemory.resetPC()
        self.updateUI()

    def stepOver(self):
        if self.ready:
            self.stepOverVar = True

    def stepIn(self):
        if self.ready:
            self.stepInVar = True

    def extClk(self, val):
        if not self.t0cs: return
        t0se = self.dMemory.memory[1][0x01][3]
        self.flankeVal = val
        if t0se == 1:
            if self.flankeVal == 1:
                return
            #1 fallend, 0 steigend
        else:
            if self.flankeVal == 0:
                return
        self.flankeClock += 1
        if not self.psa and self.flankeClock%self.scaling != 0:
            return
        self.dMemory.incTimer0()

    def updateUI(self):
        self.update_signal.emit(self.dMemory.getW())
        # self.update_signal.emit({
        #         "clock": self.clock,
        #         "timer": self.timer,
        #         "w_register": self.dMemory.getW(),
        #         "memory": self.getMemInHex(),
        #         "pcl": self.dMemory.getPCL(),
        #     })
    def getStack(self):
        return self.stack.get()
    
    def getUiInfo(self):
        return (self.dMemory.readRegister(4),#fsr
            self.dMemory.getPCL(),#pcl,
            self.lastPC,
            int(("".join([str(x) for x in self.dMemory.memory[1][0x0A]])),2),#pclath,
            self.dMemory.getPCounter(),#pc
            self.dMemory.readRegister(3),#status
            len(self.stack.stack))#stackp

if __name__ == "__main__":
    test = CPU()
    test.load_program()
    test.execute()
