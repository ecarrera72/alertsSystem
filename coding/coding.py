import sys
from datetime import *

class coding():
    
    def __init__(self):
        if len(sys.argv) >= 3:
            if sys.argv[1] == "encode": self.encode(sys.argv[2])
            if sys.argv[1] == "decode": self.decode(sys.argv[2], sys.argv[3])
    
    def encode(self, encodeVal):
        value = "".join([hex(ord(val)) for val in encodeVal])
        time = hex((datetime.now() - datetime(1900, 1, 1)).days)
        string = int((time[:4] + value + time[4:]).replace("0x", ""), 16)

        if len(sys.argv) >= 3: print(string)
        return string
    
    def decode(self, decodeVal, time):
        value = hex(int(decodeVal)).replace("0x", "")
        valueTime = (datetime.strptime(time, '%Y-%m-%d') - datetime(1900, 1, 1)).days
        try:
            val = value[2:-2]
            valTime = int(value[:2] + value[-2:], 16)
        except ValueError:
            val = value[2:-3]
            valTime = int(value[:2] + value[-3:-1], 16)

        if valTime == valueTime:
            string = "".join([chr(int(val[a:a+2], 16)) for a in range(0, len(val), 2)])

            if len(sys.argv) >= 3: print(string)
            return string

coding()