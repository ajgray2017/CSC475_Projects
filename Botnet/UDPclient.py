from socket import *
import pickle

serverName = '127.0.0.1'
serverPort = 12000
client = socket(AF_INET, SOCK_DGRAM)

input("ready? ")

client.sendto("Slave Running".encode(),(serverName, serverPort))
data, serverAddress = client.recvfrom(2048)

work = pickle.loads(data)

if work.sendEmail():
    client.sendto("Email Sent".encode(),(serverName, serverPort))
else:
    client.sendto("Failure".encode(),(serverName, serverPort))

client.close()