import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 클래스의 생성자에 소켓 그룹, 소켓 타입 지정하여 소켓 객체 생성
    print(f"Default socket timeout: {s.gettimeout()}")  # 소켓의 기본 timeout 값 얻기 (기본 값은 None -> '블로킹 모드': 데이터가 도착할 때까지 무한정 기다림)
    s.settimeout(100)  # 소켓의 기본 timeout 값 변경 (초 단위 실수), 데이터 도착 전 최대 100초까지 기다리고, 그 외에는 socket.timeout 오류 발생 (timeout 설정된 블로킹 모드)
    print(f"Current socket timeout: {s.gettimeout()}")

if __name__=='__main__':
    test_socket_timeout()

# Default socket timeout: None
# Current socket timeout: 100.0

'''
AF_INET: IPv4 주소 체계 사용하겠다는 뜻
SOCK_STREAM: TCP(수신 확인) 프로토콜 쓰겠다는 뜻
블로킹: 오청 오기 전까지 무한정 기다림 (None)
논블로킹: 즉시 반응, 요청 없으면 바로 오류 (0.0)
타임아웃: 일정 시간 기다렸다가 오류 발생 (실수)
'''