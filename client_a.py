import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = input("tcpClientA: Digite uma mensagem para passar para o Server ou exit para sair:") 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE)
    data = tcpClientA.recv(BUFFER_SIZE)
    print("Client2 recebendo dados:", data)
    MESSAGE = input("tcpClientA: Digite uma mensagem para passar para o Server ou exit para sair:")

tcpClientA.close()