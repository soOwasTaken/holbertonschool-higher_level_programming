#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tuple1 = 0
        tuple2 = None
        return tuple1, tuple2
    else:
        tuple1 = len(sentence)
    if sentence[0] == None:
        tuple2 = None
        return tuple1, tuple2
    tuple2 = sentence[0]
    return tuple1, tuple2
