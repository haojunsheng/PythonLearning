import sys
sys.path.append("..")
from utils.class_utils import *
if __name__ == '__main__':
    encoder = Encoder()
    decoder = Decoder()
    print(encoder.encode('abcde'))
    print(encoder.encode('edcba'))