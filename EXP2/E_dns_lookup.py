import socket

host = input("Enter Website: ")

print(socket.gethostbyname_ex(host))
