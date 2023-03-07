#!/usr/bin/python3
def islower(c: str):
    ascii = ord(c)
    if ascii > 96 and ascii < 123:
        return True
    else:
        return False


def uppercase(str: str):
    upstr = ""
    for ch in str:
        if islower(ch):
            upstr += chr(ord(ch)-32)
        else:
            upstr += ch
    print("{}".format(upstr))