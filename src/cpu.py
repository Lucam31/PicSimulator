from memory import ProgramMemory, DataMemory, Stack
from decode import Decoder
from fileReader import FileReader
from alu import ALU


class CPU:
    def __init__(self):
        self.pMemory = ProgramMemory()
        self.dMemory = DataMemory()
        self.decoder = Decoder()
        self.file_reader = FileReader(self.pMemory)
        self.alu = ALU(self.dMemory)
        self.program_file = "/Testprogramme/TPicSim1.LST"


    def load_program(self):
        self.file_reader.read_and_filter_lines(self.program_file)

    def execute(self):
        for cmd in self.pMemory.read():
            inst = self.decoder.decode('0x'+str(cmd))
            print(inst)
            if 'add' in inst[0] or 'sub' in inst[0] or 'and' in inst[0] or 'ior' in inst[0] or 'xor' in inst[0]:
                # self.alu.execute(inst)
                print("ALU called")

if __name__ == "__main__":
    test = CPU()
    test.load_program()
    test.execute()