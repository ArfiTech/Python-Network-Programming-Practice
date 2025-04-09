import socket

# 어떤 포트에서 무슨 네트워크 서비스를 하는지 조사. TCP나 UDP 프로토콜 사용 가능
def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print(f"Port: {port} => service name: {socket.getservbyport(port, protocolname)}")  # tcp
    print(f"Port {53} => service name: {socket.getservbyport(53, 'udp')}")  # udp

if __name__ == '__main__':
    find_service_name()

# 각 포트에 대응하는 서비스들
# Port: 80 => service name: http
# Port: 25 => service name: smtp
# Port 53 => service name: domain

'''
http: 웹페이지 보여주는 서비스
smtp: 이메일 보내는 서비스
dns: 도메인 이름 찾아주는 서비스 (도메인을 IP 주소로 바꿀 때 사용)
+)
컴퓨터는 IP주소로 구분되고, 해당 'IP주소 안'에서 어떤 서비스에 연결할지는 '포트 번호'로 구분

ex)
(IP주소):80 => 웹브라우저가 웹페이지 요청
(IP주소):25 => 이메일 보낼 때


tcp/udp 프로토콜: 인터넷에서 데이터를 보내는 (우편 서비스) 방식
항목	TCP (편지 보낼 때 수신 확인까지 받는 방식)	    UDP (엽서처럼 확인 없이 보내는 방식)
신뢰성	높음 (데이터가 정확히 도착하는지 확인함)	    낮음 (확인하지 않음)
속도	상대적으로 느림	                              빠름
용도	웹, 이메일 등 중요한 데이터 전송	           실시간 게임, 영상 스트리밍 등 빠른 전송 중요할 때

+) 같은 port라도 프로토콜에 따라 서비스가 달라질 수 있음
'''