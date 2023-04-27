#!/usr/bin/python3

def uppercase(str):
    upper_str = ""
    for c in str:
        # Check if the character is a lowercase letter
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            # Convert lowercase letter to uppercase by adding the ASCII offset
            upper_char = chr(ord(c) - 32)
        else:
            # Otherwise, keep the uppercase character as it is
            upper_char = c
        # Append the uppercase characters to the uppercase string
        upper_str += upper_char
        # Print the uppercase string
        print("{:s}".format(upper_char), end="")
    # Print a new line
    print("\n", end="")
