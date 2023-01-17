#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print(f"{i} = 0x{i:01x}".format(i))
        continue
    print(f"{i} = 0x{i:02x}".format(i))
s
