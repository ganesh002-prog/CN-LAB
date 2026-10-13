import socket
hostname = socket.gethostname()

# Get all address information
addresses = socket.getaddrinfo(hostname, None)

print("Hostname:", hostname)
print("All IP Addresses:")

ip_list = set()
for addr in addresses:
    ip = addr[4][0]
    ip_list.add(ip)

for ip in ip_list:
    print(ip)
