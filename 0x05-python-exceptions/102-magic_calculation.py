#!/usr/bin/python3
def magic_calculation(a, b):
    sol = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception('Too far')
            sol += a ** b / k
        except Exception:
            sol = b + a
            break
    return sol
