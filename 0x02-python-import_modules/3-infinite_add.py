#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    results = 0
    for i in sys.argv:
        results += int(i)
        print("{}".format(results))
