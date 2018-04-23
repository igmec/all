from socket import *


serverName = '192.168.1.240'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Enter a sentence here: ")
msg = str.encode(sentence)
clientSocket.send(msg)
modmsg = clientSocket.recv(1024)
print("From server: " + modmsg.decode())
clientSocket.close()
print("Done")
