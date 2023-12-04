#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[:0] = None
    length = len(sentence)
    result = sentence[:0]
    return length, result
