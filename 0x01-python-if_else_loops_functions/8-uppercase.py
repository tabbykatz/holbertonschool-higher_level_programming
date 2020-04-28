#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    for i in range(len(str)):
        if islower(str[i]):
            print(chr(ord(str[i]) - 32), end='')
        else:
            print(str[i], end='')
            continue
    print('')
