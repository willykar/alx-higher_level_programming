#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    n = 0
    d = 0

    for i in my_list:
        n += i[0] * i[1]
        d += i[1]

    return (n / d)
