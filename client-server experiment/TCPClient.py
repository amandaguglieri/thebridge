from socket import *
serverName = "servername or ip"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = str(input("Enter a sentence in lower case: "))
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From server: ", modifiedSentence.decode())
clientSocket.close()
