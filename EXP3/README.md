# Experiment 3 — HTTP web client using TCP sockets

[Back to experiment index](../README.md)

The supplied document is titled “HTTP Web Client & Server”; it contains the client program. The program connects to an existing HTTP server.

## Aim

To connect to an HTTP server through a TCP socket, send a GET request, and display the response.

## Algorithm

1. Create an IPv4 TCP socket and set a connection/read timeout.
2. Connect to the requested hostname and port.
3. Build an HTTP/1.1 GET request with Host and Connection headers.
4. Send the request with sendall().
5. Receive chunks until the server closes the connection.
6. Close the socket, decode the response, and display it.

## Program

Source file: [http_web_client.py](http_web_client.py)

Run from this experiment folder:

```bash
python3 http_web_client.py
```

The default target is `example.com` on port `80`. Edit `hostname`, `port`, and `path` at the end of the program to change the request. HTTPS requires TLS and is not implemented in this plain HTTP example.

```python
import socket
def download_web_page(hostname, port, path):
    try:
        # Create a socket object (IPv4 + TCP)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.settimeout(10)
        client_socket.connect((hostname, port))

        # Prepare HTTP GET request
        request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"

        # Send request to server
        client_socket.sendall(request.encode())

        # Receive response from server
        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data

        # Close the connection
        client_socket.close()

        # Decode safely (avoid Unicode error)
        return response.decode(errors="ignore")

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    hostname = "example.com"   # Plain HTTP uses port 80.
    port = 80
    path = "/"
    response = download_web_page(hostname, port, path)
    print(response)
```

## Output

Output captured against a local test HTTP server:

```text
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 14
Connection: close

Hello CN Lab!
```

The default website returns its own headers and HTML content.

## Result

The client sends an HTTP request over TCP and receives the response headers and body.

[Additional exercises from the supplied document](EXERCISES.md)
