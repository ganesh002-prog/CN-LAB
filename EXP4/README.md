# Experiment 4 — TCP echo server and client

[Back to experiment index](../README.md)

Run both programs on the same computer. Start the server first. Type `exit` in the client to end its session. This classroom example handles one client at a time and demonstrates short messages.

## A — Echo server

### Aim

To receive messages from a TCP client and send the same bytes back.

### Algorithm

1. Create an IPv4 TCP socket and enable address reuse.
2. Bind to 127.0.0.1 on port 65432 and listen.
3. Accept a client connection.
4. Receive data and echo the received bytes using sendall().
5. Continue until the client disconnects, then accept another client.
6. Stop the server with Ctrl+C and close the socket.

### Program

Source file: [A_echo_server.py](A_echo_server.py)

Start the server in terminal 1:

```bash
python3 A_echo_server.py
```

```python
import socket
def echo_server():
    try:
        # Create TCP socket (IPv4 + TCP)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allow address reuse (prevents "Address already in use" error)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind to localhost and port
        server_socket.bind(('127.0.0.1', 65432))

        # Listen for incoming connections
        server_socket.listen(5)
        print("Server listening on port 65432...")

        while True:
            # Accept client connection
            connection, client_address = server_socket.accept()
            print(f"Connected by {client_address}")

            while True:
                # Receive data
                data = connection.recv(1024)
                if not data:
                    break

                message = data.decode()
                print(f"Received: {message}")

                # Send back same data (Echo)
                connection.sendall(data)

            connection.close()
            print("Client disconnected\n")

    except KeyboardInterrupt:
        print("\nServer stopped manually.")
    except Exception as e:
        print("Error:", e)
    finally:
        server_socket.close()
if __name__ == '__main__':
    echo_server()
```

### Output

Illustrative server output; the client port varies:

```text
Server listening on port 65432...
Connected by ('127.0.0.1', 50000)
Received: Hello CN Lab
Received: exit
Client disconnected
```

### Result

The server returns the received data to the client over the TCP connection.

## B — Echo client

### Aim

To send messages to the echo server and display the returned messages.

### Algorithm

1. Create a TCP socket and connect to localhost on port 65432.
2. Read a message from the user; skip empty input.
3. Send the encoded message to the server.
4. Receive and display the echoed response.
5. Repeat until the message is exit.
6. Close the socket.

### Program

Source file: [B_echo_client.py](B_echo_client.py)

Start the client in terminal 2:

```bash
python3 B_echo_client.py
```

```python
import socket

def echo_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect(('localhost', 65432))

    while True:
        # Send data to the server
        message = input("Enter a message: ")
        if not message:
            continue
        client_socket.sendall(message.encode())
        # Receive the echo response from the server
        data = client_socket.recv(1024)
        print(f"Echoed from server: {data.decode()}")
        if message.lower() == 'exit':
            break

    client_socket.close()

if __name__ == '__main__':
    echo_client()
```

### Output

Captured client output from a local test:

```text
Enter a message: Enter a message: Echoed from server: Hello CN Lab
Enter a message: Echoed from server: exit
```

### Result

The client receives the same short messages that it sends to the echo server.

[Additional exercises from the supplied document](EXERCISES.md)
