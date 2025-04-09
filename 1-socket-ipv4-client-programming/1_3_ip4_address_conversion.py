import socket
from binascii import hexlify

# ip 주소를 32비트의 패킷 바이너리 포맷으로 변환. low-level 네트워크에서 사용 위함
def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)  # ip주소 -> 32비트(4bit * 8) 바이너리
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)  # 32비트 바이너리 -> ip 주소
        print(f"IP Address: {ip_addr} => Packed: {hexlify(packed_ip_addr)}, Unpacked: {unpacked_ip_addr}")
        # hexlify: 바이너리 데이터를 16진수 포맷으로 표현
        print(packed_ip_addr)

if __name__ == '__main__':
    convert_ip4_address()
    # IP Address: 127.0.0.1 => Packed: b'7f000001', Unpacked: 127.0.0.1
    # IP Address: 192.168.0.1 => Packed: b'c0a80001', Unpacked: 192.168.0.1

    # packed_ip_addr
    # b'\x7f\x00\x00\x01'
    # b'\xc0\xa8\x00\x01'