import sys
import struct
import math
from PIL import Image
from io import BytesIO

class PngEncoder:

    def __init__(self):
        self.minw = 10
        self.minh = 10
        self.dep = 3
        self.mode = 'RGB'


    
    def encode_png(self, data):    
        data = struct.pack('<I', len(data)) + data
        
        minsz = self.minw * self.minh * self.dep
        if len(data) < minsz:
            data += b'\0' * (minsz - len(data))
        
        side = math.ceil(math.sqrt(len(data) / self.dep))
        total = side * side * self.dep
        if len(data) < total:
            data += b'\0' * (total - len(data))
        
        img = Image.frombytes(self.mode, (side, side), data)
        bio = BytesIO()
        img.save(bio, 'png')
        return bio.getvalue()
    
    def decode_png(self, data):
        img = Image.open(BytesIO(data))
        data = img.tobytes()
        
        sz = struct.unpack('<I', data[:4])[0]
        data = data[4:4+sz]
        return data
    
    encode = encode_png
    
    def decode(self, data):

        return self.decode_png(data)

    

def bianma(fname):
    fname=fname
    
    bmlastfile = './bmlastfile/'

    data = open(fname, 'rb').read()
    encoder = PngEncoder()
    data = encoder.encode(data)
    
    fname2 = bmlastfile+'333' + '.png'

    with open(fname2, 'wb') as f:
        f.write(data)


def jiema(fname):
    fname = fname
    jmlastfile = './jmlastfile/'

    data = open(fname, 'rb').read()
    encoder = PngEncoder()

    data = encoder.decode(data)

    fname = jmlastfile+fname + '.data'
    with open(fname, 'wb') as f:
        f.write(data)
        
if __name__ == '__main__':
    bianma('./tmp/output003.png')
