#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    if len(sentence) > 0:
        ch = sentence[0]
        length = len(sentence)
    else:
        ch = None
    return length, ch
