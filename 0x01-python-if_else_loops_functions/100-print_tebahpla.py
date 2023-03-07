#!/usr/bin/python3
for i in range(26):
    print("{}".format(chr(122 - i - (32 * (i % 2)))), end="")
