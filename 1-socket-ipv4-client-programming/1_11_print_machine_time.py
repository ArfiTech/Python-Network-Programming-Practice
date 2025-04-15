import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()  # NTP 클라이언트 생성
    response = ntp_client.request('pool.ntp.org')  # NTP 서버인 pool.ntp.org에 NTP 요청 전송
    print(ctime(response.tx_time))  # Tue Apr 15 13:58:58 2025

if __name__=='__main__':
    print_time()