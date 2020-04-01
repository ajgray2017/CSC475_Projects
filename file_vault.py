import os
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename, cipher):
    chunksize = 64 * 1024
    outputFile = filename + ".enc"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    with open(filename, "rb") as infile:
        with open(outputFile, "wb") as outfile:
            outfile.write(filesize.encode("utf-8"))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b" " * (16 - (len(chunk) % 16))

                outfile.write(cipher.encrypt(chunk))

def decrypt(key, filename, cipher):
    chunksize = 64 * 1024
    outputFile = "decrypted_" + os.path.splitext(filename)[0]

    with open(filename, "rb") as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        with open(outputFile, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(cipher.decrypt(chunk))
                outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password.encode("utf-8"))
    return hasher.digest()

def main():

    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    enType = input("Choose method: (1) AES, (2) DES, (3) 3DES: ")

    if enType == 1:
        cipher = AES.new(key, AES.MODE_CBC, IV)
    elif enType == 2:
        cipher = AES.new(key, DES.MODE_CBC, IV)
    elif enType == 3:
        cipher = AES.new(key, AES.MODE_CBC, IV)
    else:
        print("Incorrect selection")

    if choice.lower() == "e":
        filename = input("File to encrypt: ")
        password = input("Password: ")
        
        encrypt(getKey(password), filename, cipher)

        print("Done encrpyting")
    
    elif choice.lower() == "d":
        filename = input("File to decrypt: ")
        password = input("Password: ")
        
        decrypt(getKey(password), filename, cipher)

        print("Done decrpyting")

if __name__ == "__main__":
    main()
