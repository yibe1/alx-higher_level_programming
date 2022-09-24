#!/usr/bin/python3
j = 25
for i in range(97, 123):
    num = 97 + j
    if(num % 2 == 0):
        ch = chr(num)
    else:
        ch = chr(num - 32)
    print("{}".format(ch), end='')
    j -= 1
