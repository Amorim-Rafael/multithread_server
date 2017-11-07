import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = input("tcpClientB: Digite uma mensagem para passar para o Server ou exit para sair:")
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE)
    data = tcpClientB.recv(BUFFER_SIZE)
    print("Client recebendo dados:", data)
    MESSAGE = input("tcpClientB: Digite uma mensagem para passar para o Server ou exit para sair:")

tcpClientB.close() 