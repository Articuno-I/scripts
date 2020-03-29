#!/usr/bin/env python3

import sys

def parseArgs(argv):
    try:
        nums = [int(argv[0]) - 1]
        sep = ' '
    except ValueError:
        nums = []
        sep = argv[0]
    except IndexError:  # No args
        exit(0)
    try:
        for arg in argv[1:]:
            nums.append(int(arg) - 1)
    except ValueError:
        print("Error: %s is not an integer." % arg, file=sys.stderr)
        exit(-1)
    return sep, nums

def main(argv):
    sep, nums = parseArgs(argv)
    for line in sys.stdin:
        line = line.strip()
        parts = line.split(sep)
        toPrint = []
        for num in nums:
            try:
                toPrint.append(parts[num])
            except IndexError:
                pass
        if toPrint:
            print(' '.join(toPrint))

if __name__ == '__main__':
    main(sys.argv[1:])
