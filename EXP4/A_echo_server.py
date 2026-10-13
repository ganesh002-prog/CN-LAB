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
