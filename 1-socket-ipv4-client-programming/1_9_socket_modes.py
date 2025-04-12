import socket

def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(True)  # True: 블로킹 (무한 대기), False: 논블로킹 (즉시 포기)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))  # 로컬 주소 IP에 바인딩(s라는 소켓을 해당 주소(IP+포트)에 연결하겠다는 뜻), 포트 번호=0: OS가 자동으로 빈 포트 하나 골라 줌

    socket_address = s.getsockname()
    print(f"Trivial Server launched on socket: {str(socket_address)}")  # Trivial Server launched on socket: ('127.0.0.1', 46123)
    # while True:
    #     s.listen(1)
    s.listen(1)  # 클라이언트 접속을 받을 준비 상태, 값: 동시 접속 허용 수
    conn, addr = s.accept()  # 클라이언트와 연결된 후. conn: client_socket, addr: client_address, 지금은 timeout 뜰 것임
    print(f"{conn=}, {addr=}")
    
if __name__ == '__main__':
    test_socket_modes()