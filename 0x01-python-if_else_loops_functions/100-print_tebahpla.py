#!/usr/bin/python3


for alpha in reversed(range(97, 123)):
    if alpha % 2 == 0:
        alpha -= 32
    print(f"{chr(alpha)}", end="")
