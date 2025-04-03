

class Decoder:
    def __init__(self):
        #masken
        self.mask1 = 0x3800 #11 1000 0000 0000
        self.mask2 = 0x3C00 #11 1100 0000 0000
        self.mask3 = 0x3E00 #11 1110 0000 0000
        self.mask4 = 0x3F00 #11 1111 0000 0000
        self.mask5 = 0x3F80 #11 1111 1000 0000
        self.valmask1 = 0x7FF #00 0111 1111 1111
        self.mask8 = 0xFF #00 0000 1111 1111
        self.fmask = 0x7F #00 0000 0111 1111 da normal dest bit
        self.bitmask = 0x380 #00 0011 1000 0000
        self.nop = 0x3F9F #wenn 0 dann nop

        self.destMask = 0x80

        # hardcoded
        self.clrwdt = 0x64 #wenn das = cmd dann clrwdt
        self.retfie = 0x9 
        self.ret = 0x8
        self.sleep = 0x63

    def getDestBit(self, cmd) -> int:
        return 1 if ((cmd & self.destMask) > 0) else 0
    
    def getBit(self, cmd) -> int:
        masked = int(cmd & self.bitmask)
        return masked >> 7

    def decode(self, cmd: hex) -> tuple:
        cmd = int(cmd, 16)
        if cmd == self.clrwdt: return ("clrwdt", None, 0)
        if cmd == self.retfie: return ("retfie", None, 0)
        if cmd == self.ret: return ("ret", None, 0)
        if cmd == self.sleep: return ("sleep", None, 0)
        if (cmd & self.nop) == 0: return ("nop", None, 0)

        #11 1000 0000 0000
        masked1 = cmd & self.mask1
        match masked1:
            #call
            case 0x2000:
                return ("call", cmd & self.valmask1, None)
            #goto
            case 0x2800:
                return ("goto", cmd & self.valmask1, None)
            case _:
                pass

        #11 1100 0000 0000
        masked2 = cmd & self.mask2
        match masked2:
            #bcf
            case 0x1000:
                return ("bcf", cmd & self.fmask, self.getBit(cmd))
            #bsf
            case 0x1400:
                return ("bsf", cmd & self.fmask, self.getBit(cmd))
            #btfsc
            case 0x1800:
                return ("btfsc", cmd & self.fmask, self.getBit(cmd))
            #btfss
            case 0x1C00:
                return ("btfss", cmd & self.fmask, self.getBit(cmd))
            #movlw
            case 0x3000:
                return ("movlw", cmd & self.mask8, None)
            #retlw
            case 0x3400:
                return ("retlw", cmd & self.mask8, None)
            case _:
                pass
            
        #11 1110 0000 0000
        masked3 = cmd & self.mask3
        match masked3:
            #addlw
            case 0x3E00:
                return ("addlw", cmd & self.mask8, None)
            #sublw
            case 0x3C00:
                return ("sublw", cmd & self.mask8, None)
            case _:
                pass

        #11 1111 0000 0000
        masked4 = cmd & self.mask4
        match masked4:
            #addwf
            case 0x700:
                return ("addwf", cmd & self.fmask, self.getDestBit(cmd))
            #andwf
            case 0x500:
                return ("andwf", cmd & self.fmask, self.getDestBit(cmd))
            #comf
            case 0x900:
                return ("comf", cmd & self.fmask, self.getDestBit(cmd))
            #decf
            case 0x300:
                return ("decf", cmd & self.fmask, self.getDestBit(cmd))
            #decfsz
            case 0xB00:
                return ("decfsz", cmd & self.fmask, self.getDestBit(cmd))
            #incf
            case 0xA00:
                return ("incf", cmd & self.fmask, self.getDestBit(cmd))
            #incfsz
            case 0xF00:
                return ("incfsz", cmd & self.fmask, self.getDestBit(cmd))
            #iorwf
            case 0x400:
                return ("iorwf", cmd & self.fmask, self.getDestBit(cmd))
            #movf
            case 0x800:
                return ("movf", cmd & self.fmask, self.getDestBit(cmd))
            #rlf
            case 0xD00:
                return ("rlf", cmd & self.fmask, self.getDestBit(cmd))
            #rrf
            case 0xC00:
                return ("rrf", cmd & self.fmask, self.getDestBit(cmd))
            #subwf
            case 0x200:
                return ("subwf", cmd & self.fmask, self.getDestBit(cmd))
            #swapf
            case 0xE00:
                return ("swapf", cmd & self.fmask, self.getDestBit(cmd))
            #xorwf
            case 0x600:
                return ("xorwf", cmd & self.fmask, self.getDestBit(cmd))
            #andlw
            case 0x3900:
                return ("andlw", cmd & self.mask8, None)
            #iorlw
            case 0x3800:
                return ("iorlw", cmd & self.mask8, None)
            #xorlw
            case 0x3A00:
                return ("xorlw", cmd & self.mask8, None)
            case _:
                pass
        
        #11 1111 1000 0000
        masked5 = cmd & self.mask5
        match masked5:
            #clrf
            case 0x180:
                return ("clrf", cmd & self.fmask, None)
            #clrw
            case 0x100:
                return ("clrw", None, None)
            #movwf
            case 0x80:
                return ("movwf", cmd & self.fmask, None)
            case _:
                pass

        #command not found
        return (None, None, None)
