import socket
import sys

import argparse

host = 'localhost'

def echo_client(port):
    """A simple echo client"""
    # TCP/IP 소켓 생성
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 소켓을 서버에 연결
    server_address = (host, port)
    print(f"Connecting to {server_address[0]} port {server_address[1]}")
    sock.connect(server_address)

    # send data
    try:
        # Send data
        message = "Test message. This will be echoed"
        print(f"Sending {message}")
        sock.sendall(message.encode())  # 문자열 -> 바이트 (default: UTF-8)
        # 응답 대기
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)  # 16바이트씩 서버 응답 읽음. 영어는 한 문자 당 1바이트
            amount_received += len(data)
            print(f"Received: {data}")
    except socket.error as e:
        print(f"Socket error: {str(e)}")
    except Exception as e:
        print(f"Other exception: {str(e)}")
    finally:
        print(f"Closing connection to the server")
        sock.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)

# python 1-socket-ipv4-client-programming/1_13b_echo_client.py --port=9900
# Connecting to localhost port 9900
# Sending Test message. This will be echoed
# Received: b'Test message. Th'
# Received: b'is will be echoe'
# Received: b'd'
# Closing connection to the server