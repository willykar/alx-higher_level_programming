#!/usr/bin/python3


def safe_print_division(a, b):
    """
    function that divides 2 integers and prints the results
    """
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
