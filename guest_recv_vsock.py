#!/usr/bin/env python3
# guest_recv_vsock.py
import socket
import os

HOST_CID = socket.VMADDR_CID_ANY  # aceita conexões de host
PORT = 12345
OUTFILE = "/tmp/received_malware.bin"

s = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
s.bind((HOST_CID, PORT))
s.listen(1)
print("VSOCK listener no guest aguardando na porta", PORT)
conn, addr = s.accept()
print("Conexão recebida de", addr)
with open(OUTFILE, "wb") as f:
    while True:
        data = conn.recv(64*1024)
        if not data:
            break
        f.write(data)
conn.close()
s.close()
print("Ficheiro recebido ->", OUTFILE)
