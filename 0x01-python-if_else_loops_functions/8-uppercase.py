#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(x):
        y = ord(str[i])
        if y < 97 and y > 122:
            print(str[i],end='')
        else:
            print("{}".format(chr(ord(str[i])-32)),end='')
