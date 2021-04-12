#! /usr/bin/env python

def collatz(x: int = 0):
    v = x
    while v > 2:
        yield v
        v = int(v / 2 if (v % 2 == 0) else (3 * v) + 1)
    yield 1
            
if __name__ == '__main__':
    import sys
    print([list(collatz(x)) for x in
        (int(v) for v in sys.argv if v.isnumeric())])
