from socket import *
import smtplib, ssl
import getpass

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')

clientSocket.sendto(message.encode(),(serverName, serverPort))
lst, serverAddress = clientSocket.recvfrom(2048)
sender_email, receiver_email, dummy_file, = lst[0], lst[1], lst[2] 
clientSocket.close()

# choosing the smtp port
port = 465 
pswrd = getpass.getpass()       # getpass function that will get the password w/o showing it

# Create SSL context
context = ssl.create_default_context()

# opens up the txt file and fills the message variable with info from the file
with open(dummy_file) as line:
    for x in line:
        message += x

print(message)      # check that the message is being pulled from the dummy txt file

# makes sure that the connection is severed when complete
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, pswrd)
    print("Sending messages")
    server.sendmail(sender_email, receiver_email, message)