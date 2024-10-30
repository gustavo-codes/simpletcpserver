from socket import *

HOST = "127.0.0.1"
PORT = 50007

serverSocket = socket(AF_INET,SOCK_STREAM) #AF_INET IPV4, SOCK_STREAM TCP
serverSocket.bind(('',PORT))
serverSocket.listen(1)
while 1:
    connectionSocket,addr = serverSocket.accept()
    print("Connected to: ")
    print(addr)
    req = connectionSocket.recv(1024).decode('utf-8')
    operation = req.split(',')
    
    res = ""

    if(operation[0]=='+'):
        res = str(int(operation[1]) + int(operation[2]))
    elif(operation[0]=='-'):
        res = str(int(operation[1]) - int(operation[2]))
    elif(operation[0]=='*'):
        res = str(int(operation[1]) * int(operation[2]))
    elif(operation[0]=='/'):
        res = str(int(operation[1]) / int(operation[2]))
    else:
        res = "Bad Request"
    

    connectionSocket.send(res.encode('utf-8'))
    connectionSocket.close()
    

