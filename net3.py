import socket
import struct

ADDR = "127.0.0.1"
PORT = 2996

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR, PORT))

message = struct.pack(">H", 0x1f) + struct.pack("<B", 0x17) + struct.pack("<B", 0x05) + "net3" + struct.pack("<B", 0x00) + struct.pack("<B", 0x0d) + "awesomesauce" + struct.pack("<B", 0x00) + struct.pack("<B", 0x09) + "password" + struct.pack("<B", 0x00)

print len(message) 

s.send(message)
print s.recv(1024)
