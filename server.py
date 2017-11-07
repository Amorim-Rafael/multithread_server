import socket
from threading import Thread
from socketserver import ThreadingMixIn

class ClientThread(Thread):
    def __init__(seft, ip, port):
        Thread.__init__(seft)
        ip = ip
        port = port
        print("Novo server socket thread iniciado em " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            print("Server recebendo os dados:", data)
            MESSAGE = input("Multithread server. Digite uma mensagem para passar para o Server ou exit para sair:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE.encode())

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print("Multithreaded server : Aguardando as connecções de clientes TCP...")
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 