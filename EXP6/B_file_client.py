import socket
from pathlib import Path


def file_transfer_client():
    filename = input("Enter the filename to send: ")
    path = Path(filename)
    if not path.is_file():
        print(f"Error: File '{filename}' not found.")
        return
    if '\n' in path.name or '\r' in path.name:
        print("Error: Filename cannot contain a newline.")
        return
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('127.0.0.1', 12345))
            client_socket.sendall((path.name + '\n').encode('utf-8'))
            with path.open('rb') as file:
                while True:
                    chunk = file.read(1024)
                    if not chunk:
                        break
                    client_socket.sendall(chunk)
            client_socket.shutdown(socket.SHUT_WR)
        print(f"File '{filename}' sent successfully.")
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    file_transfer_client()
