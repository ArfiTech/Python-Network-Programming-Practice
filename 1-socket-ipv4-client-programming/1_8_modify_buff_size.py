import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

# 소켓 버퍼 크기 변경
# 소켓 버퍼: 네트워크로 데이터를 보내거나 받을 때, 일시적으로 데이터를 보관하는 임시 장소
def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(f"Buffer size [Before]: {bufsize}")

    # setsockopt(): level, optname(옵션 이름), value(옵션에 대응하는 실제 값) 3개의 인자 받음
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)  # level = SOL_TCP: TCP 관련 설정 하겠다는 의미. TCP_NODELAY 같은 옵션 사용 가능. (TCP_NODELAY: 작게 나눠 보내지 말고 바로바로 보내라는 뜻(지연 최소화) => Nagle 알고리즘 비활성화) 값이 1인 것은 옵션 활성화.
    sock.setsockopt(
        socket.SOL_SOCKET,  # level = SOL_SOCKET: socket 자체에 관한 설정임을 의미. SO_SNDBUF나 SO_RCVBUF같은 옵션 사용 가능
        socket.SO_SNDBUF,  # 송신 버퍼: 내가 데이터를 보내면(send()), 해당 데이터는 일단 송신 버퍼에 저장 됨. 이후 OS가 네트워크를 통해 천천히 전송
        SEND_BUF_SIZE  # 송신 버퍼 크기 4096 바이트로 결정
    )
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,  # 수신 버퍼: 상대가 데이터를 보내면, 내가 읽기 전까지 해당 데이터는 소켓의 수신 버퍼에 저장. 내가 recv() 호출 시 수신 버퍼에서 꺼냄
        RECV_BUF_SIZE  # 수신 버퍼 크기 4096 바이트로 결정
    )
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print(f"Buffer size [After]: {bufsize}")

if __name__ == '__main__':
    modify_buff_size()

# Buffer size [Before]: 16384
# Buffer size [After]: 8192

'''
소켓 버퍼 크기 조절 이유

1. 네트워크 속도/부하에 따라 적절한 크기 필요
- 버퍼 너무 작을 시: OS 전송 속도 동일 시(실제로는 네트워크 따라 다름), 버퍼가 꽉 찼는데 아직 전송이 되지 않은 상황이라면, 버퍼 빌 때까지 나는 대기해야 함 (성능 저하)
- 버퍼 너무 클 시: 시스템 메모리 낭비 (비효율)

2. 네트워크 지연 및 패킷 크기 최적화
- 네트워크 전송 단위인 '패킷'의 크기와 소켓 버퍼 크기를 잘 맞춰줘야 함.
'''