#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list
    """
    printed = 0
    for a in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            break
    print("")
    return (printed)
