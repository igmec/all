from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("Server ready to receive")

while(1):
    connectionSocket, addr = serverSocket.accept()
    msg = connectionSocket.recv(1024)
    message = msg.decode()
    upperMsg = str.encode(message.upper())
    connectionSocket.send(upperMsg)
    connectionSocket.close()
    break
serverSocket.close()
print("Done")
    
