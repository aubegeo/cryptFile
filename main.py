
from hashlib import sha256

ifile = input("Select file to encrypt : ")
ofile = input("name of the output file : ")
key = input("choose a key : ")
keys = sha256(key.encode('utf-8')).digest()
with open(ifile,'rb') as inputfile :
    with open(ofile, 'wb') as outputfile :
        i = 0
        while inputfile.peek():
            c = ord(inputfile.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            outputfile.write(b)
            i = i +1
