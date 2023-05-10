#!/usr/bin/python3
# Function returns a tuple with the length of a string and its first character

def multiple_returns(sentence):
    lens = len(sentence)
    f_char = sentence[0]
    tup = (lens, f_char)
    if sentence == []:
        f_char = None
    return tup
