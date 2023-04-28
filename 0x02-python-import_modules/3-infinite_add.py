#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of addition of all arguments."""
import sys

count = 0

for num in range(1, len(sys.argv)):
    count += int(sys.argv[num])
print("{}".format(count))
