#!/usr/bin/python3
'''Prints the alphabet in lowercase except q and e'''
for letters in range(97, 123):
    if (chr(letters)) != 'q' and (chr(letters)) != 'e':
        print("{}".format(chr(letters)), end="")
