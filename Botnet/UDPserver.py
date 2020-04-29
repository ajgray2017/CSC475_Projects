from socket import *
import pickle
import smtp

def main():
    serverPort = 12000
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(('', serverPort))

    sender_email = "hellotest001smtp@gmail.com"
    receiver_email = "hellotest002smtp@gmail.com"
    testFile = "email_body.txt"
    password = "csc475assignment"

    print('The server is ready to destroy your enemies and get arrested for wire fraud')

    while True:
        input("Start Server? ")
        message, clientAddress = server.recvfrom(2048)
        print(message.decode())

        virus = smtp.SMTP(sender_email, receiver_email, password)

        payload = pickle.dumps(virus)

        server.sendto(payload, clientAddress)

        # message, clientAddress = server.recvfrom(2048)
        # print(message.decode())

if __name__ == "__main__":
    main()