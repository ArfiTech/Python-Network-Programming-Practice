import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    """A simple echo server"""
    # TCP 소켓 생성
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # address/port 재사용 가능
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 소켓을 포트에 바인딩
    server_address = (host, port)
    print(f"Starting up echo server on {server_address[0]} port {server_address[1]}")
    sock.bind(server_address)
    # client들을 listen 시작, backlog argument는 queue에 대기중인 연결들의 최대 수를 지정정.
    sock.listen(backlog)
    while True:
        print(f"Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print(f"Data: {data}")
            client.send(data)  # client에게 받은 메세지를 그대로 돌려보냄
            print(f"sent {data} bytes back to {address}")
            # end connection
            client.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)

# python 1-socket-ipv4-client-programming/1_13a_echo_server.py --port=9900
# Starting up echo server on localhost port 9900
# Waiting to receive message from client

# 클라이언트가 대기열에 오를 때까지 대기

# Data: b'Test message. This will be echoed'
# sent b'Test message. This will be echoed' bytes back to ('127.0.0.1', 34032)
# Waiting to receive message from client