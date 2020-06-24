import socket
import time

s = socket.socket()
s.connect(("localhost", 7783))
e = chr(27)
clear = e+"[1;1H"+e+"[2J"+e+"[3J"


def spring():
    s.send(b"spring")
    print(s.recv(1024).decode())


def mass():
    s.send(b"mass")
    print(s.recv(1024).decode())


def mass_spring():
    s.send(b"mass|spring")
    print(s.recv(1024).decode())


for i in range(30):
    mass_spring()
    time.sleep(0.1)
    # print(clear)

s.close()
