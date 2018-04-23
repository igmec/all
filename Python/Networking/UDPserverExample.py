from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server ready to receive...")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Got msg")
    print(type(message))
    modmsg = message.decode().upper()
    print(modmsg)
    serverSocket.sendto(str.encode(modmsg), clientAddress)
    break
print("Done")
