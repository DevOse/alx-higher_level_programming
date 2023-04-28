#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of command line arguments."""
import sys
count = len(sys.argv) - 1
if count == 0:
    print(f"{count} arguments.")
if count == 1:
    print(f"{count} argument:")
else:
    print(f"{count} arguments")

for num in range(1, len(sys.argv)):
    print(f"{num}: {sys.argv[num]}")
