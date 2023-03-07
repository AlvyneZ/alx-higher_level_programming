#!/usr/bin/python3
for i in range(26):
    if i not in [4, 16]:
        print("{}".format(chr(97+i)), end="")
