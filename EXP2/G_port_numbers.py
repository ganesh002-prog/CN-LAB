import ipaddress
import socket

target = input("Enter IP Address: ").strip()
ipaddress.IPv4Address(target)

for port in range(1, 101):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.2)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port", port, "is Open")
