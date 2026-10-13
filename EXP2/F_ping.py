import ipaddress
import platform
import subprocess

host = input("Enter IP: ").strip()
# Validate the address and pass arguments directly to ping.
ipaddress.ip_address(host)
count_flag = "-n" if platform.system() == "Windows" else "-c"
subprocess.run(["ping", count_flag, "4", host], check=False)
