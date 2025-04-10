import socket
import sys

# 네트워크(빅엔디안), 호스트(리틀엔디안) 간 순서 변환
def convert_integer():
    data = 1234
    # data = 0x1234
    # 32-bit
    print(f"Original: {data} => Long host byte order: {socket.ntohl(data)}, Network byte order: {socket.htonl(data)}")
    print(f"Original: {hex(data)} => Long host byte order: {hex(socket.ntohl(data))}, Network byte order: {hex(socket.htonl(data))}")

    # 16-bit
    print(f"Original: {data} => Short host byte order: {socket.ntohs(data)}, Network byte order: {socket.htons(data)}")
    print(f"Original: {hex(data)} => Short host byte order: {hex(socket.ntohs(data))}, Network byte order: {hex(socket.htons(data))}")

if __name__ == '__main__':
    convert_integer()
    print(sys.byteorder)  # little

# Original: 1234 => Long host byte order: 3523477504, Network byte order: 3523477504
# Original: 0x4d2 => Long host byte order: 0xd2040000, Network byte order: 0xd2040000
# Original: 1234 => Short host byte order: 53764, Network byte order: 53764
# Original: 0x4d2 => Short host byte order: 0xd204, Network byte order: 0xd204

'''
ntohs 입장에서는 '1234=>0x04D2는 네트워크가 빅엔디안으로 전달 준 것이니, 호스트 입장인 리틀엔디안으로 바꿔야겠다'해서 0xD204가 되는 것 (전달 받은 값을 빅엔디안 취급, 리틀엔디안으로 바꿈)
htons 입장에서는 '1234=>0x04D2는 호스트가 리틀엔디안으로 전달 준 것이니, 네트워크 입장인 빅엔디안으로 바꿔야겠다'해서 0xD204가 되는 것 (전달 받은 값을 리틀엔디안 취급, 빅엔디안으로 바꿈)
'''