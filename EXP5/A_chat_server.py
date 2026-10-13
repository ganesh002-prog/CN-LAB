import socket
import threading
clients = []
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            # Broadcast message to all other clients
            for client in clients:
                if client != client_socket:
                    client.sendall(message.encode())
        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break
    # Remove disconnected client
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()
    print(f"{client_address} disconnected")
def chat_server():
    # Create TCP socket
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    # Allow immediate reuse of the port
    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    # Bind server to localhost and port 55555
    server_socket.bind(('localhost', 55555))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on port 55555...")
    while True:
        # Accept a new client
        client_socket, client_address = server_socket.accept()
        # Add client to the client list
        clients.append(client_socket)
        # Create a separate thread for the client
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        # Allow thread to terminate when server stops
        thread.daemon = True
        # Start client thread
        thread.start()
if __name__ == '__main__':
    chat_server()
