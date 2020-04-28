from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('The server is ready to destroy your enemies and get arrested for wire fraud')
while True:
    print("waiting...")
    message, clientAddress = serverSocket.recvfrom(2048)

    print(message)

    # sender_email = input("Sender Email.. ")
    # receiver_email = input("Receiver Email.. ")
    # dummy_file = input("File.. ")

    lst = ["hellotest002smtp@gmail.com", "hellotest001smtp@gmail.com", "email_body.txt"]

    serverSocket.sendto(lst.encode(), clientAddress)