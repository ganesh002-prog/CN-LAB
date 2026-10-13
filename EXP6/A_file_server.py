import socket
from pathlib import Path


def file_transfer_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(('127.0.0.1', 12345))
            server_socket.listen(1)
            print("Server listening on port 12345...")
            connection, client_address = server_socket.accept()
            with connection:
                print(f"Connected by {client_address}")
                # Read a complete filename line, then the remaining file bytes.
                with connection.makefile('rb') as incoming:
                    header = incoming.readline(4097)
                    if not header.endswith(b'\n') or len(header) > 4096:
                        raise ValueError("Invalid filename header")
                    filename = Path(header[:-1].decode('utf-8')).name
                    if not filename or filename in ('.', '..'):
                        raise ValueError("Invalid filename")
                    print(f"Receiving file: {filename}")
                    with open(f"received_{filename}", 'wb') as file:
                        while True:
                            data = incoming.read(1024)
                            if not data:
                                break
                            file.write(data)
                print(f"File saved as received_{filename}")
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    file_transfer_server()
