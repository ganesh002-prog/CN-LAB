# Experiment 7 — ARP and RARP simulation

[Back to experiment index](../README.md)

This is a dictionary-based simulation. It does not send real ARP or RARP packets.

## Aim

To simulate address resolution from IP to MAC and reverse resolution from MAC to IP.

## Algorithm

1. Create an ARP table mapping IP addresses to MAC addresses.
2. Build a reverse table mapping MAC addresses to IP addresses.
3. Display both tables.
4. Perform ARP lookups for known and unknown IP addresses.
5. Perform RARP lookups for known and unknown MAC addresses.
6. Add a new IP/MAC entry to both tables.
7. Display the updated tables.

## Program

Source file: [arp_rarp.py](arp_rarp.py)

Run from this experiment folder:

```bash
python3 arp_rarp.py
```

```python
class ARP_RARP_Simulator:

    def __init__(self):

        # ARP Table: IP Address -> MAC Address
        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18"
        }
        # RARP Table: MAC Address -> IP Address
        self.rarp_table = {
            mac: ip
            for ip, mac in self.arp_table.items()
        }
    # ARP: IP Address -> MAC Address
    def arp_request(self, ip_address):
        print("\n----------------------------------------")
        print("ARP REQUEST")
        print("----------------------------------------")
        print(
            f"ARP Request: Who has {ip_address}? "
            "Tell me your MAC address."
        )

# Search for IP address
        mac_address = self.arp_table.get(ip_address)

        if mac_address:

            print(
                f"ARP Reply: {ip_address} "
                f"is at {mac_address}."
            )

            return mac_address

        else:

            print(
                f"ARP Reply: {ip_address} "
                "is not found."
            )

            return None

 # RARP: MAC Address -> IP Address
    def rarp_request(self, mac_address):

        print("\n----------------------------------------")
        print("RARP REQUEST")
        print("----------------------------------------")

        print(
            f"RARP Request: Who has MAC address "
            f"{mac_address}? Tell me your IP address."
        )

        # Search for MAC address
        ip_address = self.rarp_table.get(mac_address)

        if ip_address:

            print(
                f"RARP Reply: {mac_address} "
                f"is associated with IP {ip_address}."
            )

            return ip_address

        else:

            print(
                f"RARP Reply: {mac_address} "
                "is not found."
            )

            return None

    # Display ARP Table
    def display_arp_table(self):

        print("\n========================================")
        print("ARP TABLE")
        print("========================================")

        print("IP Address\t\tMAC Address")
        print("----------------------------------------")

        for ip, mac in self.arp_table.items():

            print(f"{ip}\t\t{mac}")

    # Display RARP Table
    def display_rarp_table(self):

        print("\n========================================")
        print("RARP TABLE")
        print("========================================")

        print("MAC Address\t\t\tIP Address")
        print("----------------------------------------")

        for mac, ip in self.rarp_table.items():

            print(f"{mac}\t{ip}")

    # Add new IP and MAC entry
    def add_entry(self, ip_address, mac_address):

        self.arp_table[ip_address] = mac_address
        self.rarp_table[mac_address] = ip_address

        print("\nEntry added successfully.")

        print(f"IP  : {ip_address}")
        print(f"MAC : {mac_address}")

# Main Program
if __name__ == "__main__":

    # Create simulator
    simulator = ARP_RARP_Simulator()

    print("\n==============================================")
    print("          ARP AND RARP SIMULATOR")
    print("==============================================")

    # Display ARP table
    simulator.display_arp_table()

    # Display RARP table
    simulator.display_rarp_table()

    # ARP Examples
    print("\n========== ARP EXAMPLES ==========")

    simulator.arp_request("192.168.1.1")

    simulator.arp_request("192.168.1.2")

    simulator.arp_request("192.168.1.100")

    # RARP Examples
    print("\n========== RARP EXAMPLES ==========")

    simulator.rarp_request(
        "00:0a:95:9d:68:16"
    )

    simulator.rarp_request(
        "00:0a:95:9d:68:17"
    )

    simulator.rarp_request(
        "00:0a:95:9d:68:99"
    )

    # Add new entry
    print("\n========== ADD NEW ENTRY ==========")

    simulator.add_entry(
        "192.168.1.4",
        "00:0a:95:9d:68:19"
    )

    # Display updated tables
    simulator.display_arp_table()

    simulator.display_rarp_table()
```

## Output

Output screenshots from the supplied slides:

![Initial ARP table](images/output_1.png)

![Initial RARP table](images/output_2.png)

![ARP lookups](images/output_3.png)

![RARP lookups](images/output_4.png)

![Adding an entry](images/output_5.png)

![Updated ARP and RARP tables](images/output_6.png)

The program also prints “is not found” for unknown addresses.

## Result

The simulation resolves known addresses in both directions, reports missing entries, and displays the newly added mapping.
