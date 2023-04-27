#!/usr/bin/python3

def remove_char_at(str, n):
    str_copy = ""
    for i in range(len(str)):
        if i != n:
            str_copy += str[i]
    return (str_copy)

x = remove_char_at("oises", 2)
print(x)
