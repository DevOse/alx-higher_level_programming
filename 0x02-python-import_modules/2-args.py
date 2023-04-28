#!/usr/bin/python3

import sys
count = len(sys.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))

for num in range(1, len(sys.argv)):
    print("{}: {}".format(num, sys.argv[num]))
