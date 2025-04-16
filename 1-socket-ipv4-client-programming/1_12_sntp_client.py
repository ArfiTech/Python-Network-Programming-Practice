import socket
import struct
import time

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800  # NTP 시간(1900/1/1)과 Unix 시간(1970/1/1) 사이의 초 차이이

# SNTP 클라이언트 작성
def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP 소켓 생성
    data = b'\x1b' + 47 * b'\0'  # SNTP 프로토콜 데이터 (SNTP 요청 메시지를 만들기 위한 정해진 형식의 48바이트 데이터), \x 뒤에는 두 자리 16진수 와야 함.(1b(16) = 27(10))
    # '\x1b'는 버전 + 모드 같은 걸 설정한 1바이트, 나머지 47 바이트는 0으로 채움 (초기화된 요청)
    client.sendto(data, (NTP_SERVER, 123))  # 패킷에 담아 전송. data: 48바이트의 애플리케이션 계층의 데이터 패킷, (NTP_SERVER, 123): 목적지 서버 주소와 포트 번호
    '''
    실제 네트워크 전송 시
    [UDP 헤더] + [NTP 데이터 48바이트] → UDP 패킷
    [IP 헤더] + [UDP 패킷] → IP 패킷
    '''
    data, address = client.recvfrom(1024)  # 1024: 받을 수 있는 최대 바이트 수
    if data:
        print(f"Response received from: {address}")
    t = struct.unpack('!12I', data)[10]  # !12I: 12개의 4바이트 정수(48바이트)로 해석, [10]: 전송 시간의 초 단위(서버가 응답을 보낸 시각)
    t -= TIME1970  # 현재 시간(Unix 시간) 기준으로 맞추기기
    print(f"\tTime={time.ctime(t)}")

if __name__=='__main__':
    sntp_client()

# Response received from: ('185.103.117.60', 123)
# Time=Wed Apr 16 12:44:08 2025

'''
포트 번호
프로토콜	포트 번호	    설명
HTTP	    80	        웹서버
HTTPS	    443	        암호화된 웹
DNS	        53	        도메인 질의
NTP	        123	        시간 동기화 요청
'''