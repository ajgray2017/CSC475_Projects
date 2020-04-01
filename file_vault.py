import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def AESencrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename + ".enc"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

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

                outfile.write(encryptor.encrypt(chunk))


def AESdecrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = "decrypted_" + os.path.splitext(filename)[0]

    with open(filename, "rb") as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(filesize)


def getKey(password):
    hasher = SHA256.new(password.encode("utf-8"))
    return hasher.digest()


def main():

    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    en_type = input("Choose method: (1) AES, (2) DES, (3) 3DES")

    if choice.lower() == "e":
        filename = input("File to encrypt: ")
        password = input("Password: ")
        if en_type == 1:
            AESencrypt(getKey(password), filename)
        if en_type == 2:
            DESencrypt(getKey(password), filename)
        if en_type == 3:
            TDESencrypt(getKey(password), filename)

    elif choice.lower() == "d":
        filename = input("File to decrypt: ")
        password = input("Password: ")
        if en_type == 1:
            AESdecrypt(getKey(password), filename)
        if en_type == 2:
            DESdecrypt(getKey(password), filename)
        if en_type == 3:
            TDESdecrypt(getKey(password), filename)


if __name__ == "__main__":
    main()
