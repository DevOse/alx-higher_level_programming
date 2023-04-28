#!/usr/bin/python3

import sys
count = len(sys.argv) - 1
if count == 1:
    print(f"{count} argument:")
else:
    print(f"{count} arguments")

for num in range(1, len(sys.argv)):
    print(f"{num}: {sys.argv[num]}")
