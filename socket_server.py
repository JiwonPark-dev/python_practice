# 쓰레드를 이용한 소켓 서버 클라이언트
import socket
import threading

s = socket.socket()
address = ("", 2500)
s.bind(address)
s.listen(1)
print('Waiting')
c_socket, c_addr = s.accept()
print("Connection from", c_addr)


def server_socket():
    while True:
        data = c_socket.recv(1024).decode()
        print("\n")
        print("클라이언트 : ", data)
        print("Sending message : ")


def server_socket_receive():
    while True:
        msg = input("Sending message : ")
        c_socket.send(msg.encode())


thread1 = threading.Thread(target=server_socket)
thread1.start()
thread2 = threading.Thread(target=server_socket_receive)
thread2.start()
