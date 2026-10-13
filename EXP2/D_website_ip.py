import socket

website = "www.google.com"

ip = socket.gethostbyname(website)

print("Website :", website)
print("IP Address :", ip)
