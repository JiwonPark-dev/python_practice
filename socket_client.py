# 쓰레드를 이용한 소켓 서버 클라이언트
import socket
import threading

sock = socket.create_connection(('localhost', 2500))


def client_socket():
    while True:
        msg = input("Sending message : ")
        sock.send(msg.encode())


def client_socket_receive():
    while True:
        msg = sock.recv(1024)
        print("\n")
        print(f'서버 : {msg.decode()}')
        print("Sending message : ")


thread1 = threading.Thread(target=client_socket)
thread1.start()
thread2 = threading.Thread(target=client_socket_receive)
thread2.start()
