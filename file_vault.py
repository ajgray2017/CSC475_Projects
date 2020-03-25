from Crypto.Cipher import AES
from Crypto import Random


def encryption(enType):
    if enType == 1:
        key = b"sixteen byte pas"
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        message = iv + cipher.encrypt(b"Attack at dawn")
        print(message)
    elif enType == 2:
        print("to be continued...")
    elif enType == 3:
        print("to be continued...")

def decryption(in_file, enType):
    pass

def main():
    # in_file = input("Type in the path of the file to be encrypted: ")
    eord = int(input("press 1 for encryption or 2 for decryption... "))
    usr_select = int(input("Select 1 for AES, 2 for DES, 3 for DES... "))

    if eord == 1:
        encryption(usr_select)
    elif eord == 2:
        decryption(in_file, usr_select)

if __name__ == "__main__":
    main()