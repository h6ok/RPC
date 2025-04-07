import socket
import os

class MyServer:

    def __init__(self):
        # create socket
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        # configure server address
        server_address = ''

        # bing socket to address
        sock.bing(server_address)

        self.socket = sock

    def start():
        
        #listen
        socket.listen(1)

        while True:
            conn, client_address = socket.accept()

            try:
                while True:

                    data = conn.recv(32)

                    data
                    
