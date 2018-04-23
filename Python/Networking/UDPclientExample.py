from socket import *

serverName = "192.168.1.240"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
messagebytes = str.encode(message)
print(type(messagebytes))
clientSocket.sendto(messagebytes, (serverName, serverPort))
print("message sent")
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("msg here")
print(modifiedMessage.decode())
clientSocket.close()
print("Done")
