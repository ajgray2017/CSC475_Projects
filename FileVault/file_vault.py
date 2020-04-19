import os

def encrypt(filename, cipher, IV, byteSize, enType): 
    chunksize = 64 * 1024
    outputFile = enType + "_" + filename + ".enc"
    filesize = str(os.path.getsize(filename)).zfill(byteSize)

    with open(filename, "rb") as infile:
        with open(outputFile, "wb") as outfile:
            outfile.write(filesize.encode("utf-8"))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % byteSize != 0:
                    chunk += b" " * (byteSize - (len(chunk) % byteSize))

                outfile.write(IV + cipher.encrypt(chunk))

def decrypt(filename, cipher, IV, byteSize):
    chunksize = 64 * 1024
    outputFile = "decrypted_" + os.path.splitext(filename)[0]

    with open(filename, "rb") as infile:
        filesize = int(infile.read(byteSize))
        IV = infile.read(byteSize)

        with open(outputFile, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(cipher.decrypt(chunk))
                outfile.truncate(filesize)

def getKey(password):
    from Crypto.Hash import SHA256

    hasher = SHA256.new(password.encode("utf-8"))
    return hasher.digest()

def main():
    from Crypto import Random

    #user inputs 
    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    enType = int(input("Choose method: (1) AES, (2) DES, (3) 3DES: "))
    password = input("Password: ")

    #AES encryption option
    if enType == 1:
        from Crypto.Cipher import AES

        enType = "AES"
        byteSize = 16
        IV = Random.new().read(byteSize)
        cipher = AES.new(getKey(password), AES.MODE_CBC, IV)

    #DES encryption option
    elif enType == 2:
        from Crypto.Cipher import DES

        enType = "DES"
        byteSize = 8
        IV = Random.new().read(byteSize)
        #! Figure out dynamic key
        cipher = DES.new(b"-8B key-", DES.MODE_CBC, IV)
    
    #3DES encryption option 
    elif enType == 3:
        from Crypto.Cipher import DES3

        enType = "3DES"
        byteSize = 8
        IV = Random.new().read(byteSize)
        cipher = DES3.new(b'Sixteen byte key', DES3.MODE_EAX, IV)

    else:
        print("Incorrect selection")

    if choice.lower() == "e":
        filename = input("File to encrypt: ")
        encrypt(filename, cipher, IV, byteSize, enType)
        print("Done encrpyting")

    elif choice.lower() == "d":
        filename = input("File to decrypt: ")
        decrypt(filename, cipher, IV, byteSize)
        print("Done decrypting")
        
    else:
        print("Incorrect selection")

if __name__ == "__main__":
    #! REMOVE 
    while True:
        main()
