#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    add = 0
    for result in argv[1:]:
        add = add + int(result)
    print(add)
