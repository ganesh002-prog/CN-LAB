import json
import socket
from urllib.request import urlopen

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

try:
    with urlopen("https://api.ipify.org?format=json", timeout=5) as response:
        data = json.load(response)
        public_ip = data.get("ip", "Unknown")
except Exception as e:
    public_ip = f"Unable to fetch public IP: {e}"

print("- Hostname:", hostname)
print("- Local IP:", local_ip)
print("- Public IP:", public_ip)
