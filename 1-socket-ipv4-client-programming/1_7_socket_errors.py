import sys
import socket
import argparse

# 다양한 소켓 에러
def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 + TCP로 소켓 생성 (프로그램이 네트워크를 통해 다른 컴퓨터와 통신하기 위해 여는 통로)
    except socket.error as e:
        print(f"Error creating socket: {e}")
        sys.exit(1)

    # Second try-except block -- connect to given host/port
    try:
        s.connect((host, port))  # host 서버의 port번 포트에 연결
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
        sys.exit(1)
    except socket.error as e:
        print(f"Connection error: {e}")
        sys.exit(1)

    # Third try-except block -- sending data
    try:
        s.sendall(f"GET {filename} HTTP/1.0\r\n\r\n")  # 데이터 보내기
    except socket.error as e:
        print(f"Error sending data: {e}")
        sys.exit(1)

    while True:
        # Fourth try-except block -- waiting to receive data from remote host
        try:
            buf = s.recv(2048)  # 데이터 받기
        except socket.error as e:
            print(f"Error receiving data: {e}")
            sys.exit(1)
        
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf)

if __name__=='__main__':
    main()

# python 1-socket-ipv4-client-programming/1_7_socket_errors.py -host=<HOST> --port=<PORT> --file=<FILE>
# python 1-socket-ipv4-client-programming/1_7_socket_errors.py --host=www.pytgo.org --port=8080 --file=1_7_socket_errors.py  ## 존재하지 않는 호스트 연결 시도 에러 (주소 에러) ([Errno -2] Name or service not known)
# python 1-socket-ipv4-client-programming/1_7_socket_errors.py --host=www.python.org --port=8080 --file=1_7_socket_errors.py  ## 지정 포트에 물린 서비스 없는 상태에서 해당 포트 연결 시도 에러 (연결 시간 초과 에러)
# python 1-socket-ipv4-client-programming/1_7_socket_errors.py --host=www.python.org --port=80 --file=1_7_socket_errors.py


    