import socket
import json
import callable as Call
from response import Response
import os

class MyServer:

    def __init__(self):
        # create socket
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        # configure server address
        server_address = 'localhost'

        # bing socket to address
        sock.bind(("::1", 8080))

        self.socket = sock
        self.connList = []

    def start(self):
        
        #listen
        self.socket.listen(1)

        while True:
            conn, client_address = self.socket.accept()
            self.connList.append(conn)

            try:
                while True:

                    data = conn.recv(1024)

                    data_str = data.decode('utf-8')

                    if data:
                        #parse json to dict
                        json_dict = json.loads(data_str)

                        method = json_dict["method"]
                        params = json_dict["params"]

                        try:
                            result = Call.callable_map[method](params)
                            resp = Response(result, None)
                            resp_json = resp.to_json()
                            conn.sendall(resp_json.encode())

                        except Exception as e:
                            resp = Response(None, e)
                            resp_json = resp.to_json()
                            conn.sendall(resp_json.encode())

                    else:
                        break

            finally:
                conn.close()          
