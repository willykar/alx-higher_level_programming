#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLength = len(sys.argv)
    if argLength == 1:
        print("{} arguments.".format(argLength - 1))
    elif argLength == 2:
        print("{} argument:".format(argLength - 1))
    else:
        print("{} arguments:".format(argLength - 1))
    for i in range(1, argLength):
        print("{}: {}".format(i, sys.argv[i]))
