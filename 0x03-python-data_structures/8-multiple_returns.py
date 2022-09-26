#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence != None:
        ch = sentence[0]
    else:
        ch = None
    return ch, length
