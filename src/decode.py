class Decoder:
    def __init__(self):
        #masken
        self.byteOriented = 0x3F00
        self.bitOriented = 0x3C00
        self.clrw = 0x3F80 #wenn 0x100 ergebnis ist dann clrw
        self.nop = 0x3F9F #wenn 0 dann nop

        self.rand1 = 0x3E00, 0x3F00, 0x3800, 
        # hardcoded
        self.clrwdt = 0x64 #wenn das = cmd dann clrwdt
        self.retfie = 0x9 
        self.ret = 0x8
        self.sleep = 0x63

    def decode(self, cmd: int) -> tuple:
        if cmd == self.clrwdt: return ("clrwdt", None)
        if cmd == self.retfie: return ("retfie", None)
        if cmd == self.ret: return ("ret", None)
        if cmd == self.sleep: return ("sleep", None)

        match cmd:
            case 0x01:
                return "Command 1 executed"
            case 0x02:
                return "Command 2 executed"
            case 0x03:
                return "Command 3 executed"
            case _:
                return "Unknown command"