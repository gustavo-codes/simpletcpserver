from socket import *

HOST = "127.0.0.1"
PORT = 50007

serverSocket = socket()
serverSocket.connect((HOST,PORT))
op = input('Digite a operação: ')
op1 = input('Digite o primeiro operando: ')
op2 = input('Digite o segundo operando: ')
req = op+','+op1+','+op2
serverSocket.send(req.encode('utf-8'))
res = serverSocket.recv(1024)
print(res.decode('utf-8'))
serverSocket.close()

