#!/usr/bin/python3
# Function that returns a tuple with the length of a string and its first character
#If the sentence is empty, the first character should be equal to None
#You are not allowed to import any module
def multiple_returns(sentence):
    lens = len(sentence)
    f_char = sentence[0]
    tup = (lens, f_char)
    if sentence == "":
        f_char = None
        
    return tup

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))