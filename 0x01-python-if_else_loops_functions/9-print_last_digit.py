#!/usr/bin/python3
'''A function that prints the last digit of a number given as a param'''

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
