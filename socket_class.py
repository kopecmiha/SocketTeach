import socket
import struct

from utils import Encoder


class Socket:
    socket_session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def listen(self):
        with self.socket_session as sock:
            print(f"Start Listening")
            sock.bind((self.HOST, self.PORT))
            sock.listen()
            conn, (client_host, client_port) = sock.accept()
            with conn:
                print(f"Connected by {client_host}:{client_port}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    decoded_data = self.decode(data)
                    print(decoded_data)
                    conn.sendall(b"Data succesfully")

    def send(self, data):
        with self.socket_session as sock:
            encoded_data = self.encode(data)
            sock.connect((self.HOST, self.PORT))
            sock.sendall(encoded_data)
            data = sock.recv(1024)
            print(f"{data!r}")

    def decode(self, data):
        encoded_info, encoder_format = data.split(b"#")
        decoded_data = struct.unpack(encoder_format, encoded_info)
        return decoded_data

    def encode(self, data):
        encoded_info, encoder_format = Encoder(data).encode()
        encoded_data = encoded_info + b"#" + str.encode(encoder_format)
        return encoded_data
