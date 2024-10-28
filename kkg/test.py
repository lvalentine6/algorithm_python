#!/usr/bin/env python3
import socket

# 현재 컴퓨터의 IP 주소 가져오기
def get_current_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# 파일 읽기
with open(r'C:\Users\roy\Desktop\Dev\sample_before.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 현재 IP 가져오기
current_ip = get_current_ip()

# 각 줄을 저장할 새로운 리스트
new_lines = []

# 각 줄을 확인하며 필요한 부분 수정
for line in lines:
    if 'IP:' in line:
        line = line.replace('10.1.2.3', current_ip)
    elif 'username:' in line:
        line = line.replace('test_user', 'svc_user')
    elif 'password:' in line:
        line = line.replace('mypassword', 'mypassword1@#')
    new_lines.append(line)

# 수정된 내용을 새 파일에 저장
with open(r'C:\Users\roy\Desktop\Dev\sample_after.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)