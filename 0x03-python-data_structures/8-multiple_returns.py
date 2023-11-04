#!/usr/bin/python3

def multiple_returns(sentence):
    if not bool(sentence):
        return (0, None)
    return (len(sentence), sentence[0])
