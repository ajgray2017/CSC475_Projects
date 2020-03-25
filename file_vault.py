from Crypto.Cipher import AES
from Crypto import Random
import os, struct


def encryption(in_file, enType, out_file = None, chunksize = 24*1024):
    key = b"sixteen byte pas"

    if out_file == None:
        out_file = in_file + ".enc"

    with open(in_file, "rb") as in_file:
        with open(out_file, "wb") as out_file:

            if enType == 1:
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(key, AES.MODE_CFB, iv)
                while True:
                    chunk = in_file.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b" " * (16 - len(chunk) % 16)
                    out_file.write(cipher.encrypt(chunk))

            elif enType == 2:
                print("to be continued...")
            elif enType == 3:
                print("to be continued...")

def decryption(in_file, enType, out_file = None, chunksize = 24*1024):
    key = b"sixteen byte pas"

    if out_file == None:
        out_file = "dec_" + os.path.splitext(in_file)[0]

    with open(in_file, "rb") as in_file:
        with open(out_file, "wb") as out_file:

            origsize = struct.unpack('<Q', in_file.read(struct.calcsize('Q')))[0]

            if enType == 1:
                iv = in_file.read(16)
                cipher = AES.new(key, AES.MODE_CFB, iv)
                while True:
                    chunk = in_file.read(chunksize)
                    if len(chunk) == 0:
                        break
                    out_file.write(cipher.encrypt(chunk))
                out_file.truncate(origsize)

            elif enType == 2:
                print("to be continued...")
            elif enType == 3:
                print("to be continued...")


def main():
    in_file = input("Type in the path of the file to be encrypted/decrypted: ")
    eord = int(input("press 1 for encryption or 2 for decryption... "))
    usr_select = int(input("Select 1 for AES, 2 for DES, 3 for DES... "))

    if eord == 1:
        encryption(in_file, usr_select)
    elif eord == 2:
        decryption(in_file, usr_select)

if __name__ == "__main__":
    main()