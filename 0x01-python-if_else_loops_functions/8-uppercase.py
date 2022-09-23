#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(x):
        y = ord(str[i])
        if y < 97 and y > 122:
            ch = str[i]
        else:
            ch = chr(ord(str[i])-32)
        print("{}".format(ch),end='')
    print("")
