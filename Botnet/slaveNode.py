from socket import *
import pickle

def main():
    serverName = '127.0.0.1'
    serverPort = 12000
    client = socket(AF_INET, SOCK_DGRAM)

    client.sendto("Slave Running".encode(),(serverName, serverPort))
    data, serverAddress = client.recvfrom(2048)

    work = pickle.loads(data)

    if work.sendEmail():
        client.sendto("Message Sent".encode(),(serverName, serverPort))
    else:
        client.sendto("Failure".encode(),(serverName, serverPort))

    client.close()

if __name__ == "__main__":
    main()