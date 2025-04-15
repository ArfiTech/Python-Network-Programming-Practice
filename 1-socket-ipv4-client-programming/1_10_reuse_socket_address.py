import socket

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)  # 주소(포트) 재사용 가능 여부에 대한 정보 얻기
    print(f"Old sock state: {old_state}")

    # Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # socket 관련 설정 하겠다는 의미, 주소(포트) 재사용 가능 상태로 값 변경
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print(f"New sock state: {new_state}")

    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 프로세스 종료 후 다시 연결해도 같은 포트 연결 가능
    srv.bind(('', local_port))  # 모든 인터페이스(0.0.0.0)에서 8282번 포트로 대기
    srv.listen(1)  # 클라이언트 연결 요청이 최대 1개까지만 대기열에 쌓일 수 있음
    print(f"Listening on port: {local_port}")
    while True:  # 클라이언트 연결 대기
        try:
            connection, addr = srv.accept()  # 클라이언트 연결 수락
            print(f"Connected by {addr[0]}:{addr[1]}")
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print(f"{msg}")

if __name__=='__main__':
    reuse_socket_addr()

'''
실행 시
Old sock state: 0
New sock state: 1
Listening on port: 8282

이후 다른 프로세스에서
telnet localhost 8282
하면
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.

본 프로세스에선
Connected by 127.0.0.1:40260
'''