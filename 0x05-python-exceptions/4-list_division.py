#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    a function that divides element by element 2 lists
    """
    a = 0
    new_list = []
    div = 0
    for a in range(0, list_length):
        try:
            div = (my_list_1[a] / my_list_2[a])
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            new_list.append(div)
    return new_list
