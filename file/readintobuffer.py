import os.path
import sys

def read_into_buffer(filename):
    buf=bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
      f.readinto(buf)
    return buf

if __name__=='__main__':
    content=read_into_buffer(sys.argv[0])
    print content
