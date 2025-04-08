import socket

# 외부 컴퓨터의 ip 주소 알아내기
def get_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print(f"IP address of {remote_host}: {socket.gethostbyname(remote_host)}")
    except socket.error as e:
        print(f"{remote_host}: {e}")

if __name__ == '__main__':
    get_remote_machine_info()