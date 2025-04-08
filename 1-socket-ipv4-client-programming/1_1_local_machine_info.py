import socket

# 호스트 이름과 해당 호스트의 IP 주소 출력
def print_machine_info():
    host_name = socket.gethostname()
    print(f"Host name: {host_name}")
    print(f"IP address: {socket.gethostbyname(host_name)}")

if __name__ == '__main__':
    print_machine_info()