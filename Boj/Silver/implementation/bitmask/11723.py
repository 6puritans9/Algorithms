import sys

input = sys.stdin.readline


class Bitmask:
    def __init__(self):
        self.LIMIT = 20
        self.mask = 0

    def add(self, x):
        self.mask |= (1 << x)

    def remove(self, x):
        self.mask &= ~(1 << x)

    def check(self, x):
        print(1 if (self.mask & (1 << x)) else 0)

    def toggle(self, x):
        self.mask ^= (1 << x)

    def all(self):
        self.mask = (1 << self.LIMIT) - 1

    def empty(self):
        self.mask = 0

    def exec(self, cmd, x=None):
        if cmd == "add":
            self.add(x)
        elif cmd == "remove":
            self.remove(x)
        elif cmd == "check":
            self.check(x)
        elif cmd == "toggle":
            self.toggle(x)
        elif cmd == "all":
            self.all()
        elif cmd == "empty":
            self.empty()


if __name__ == "__main__":
    # 1. An empty set S is given.
    # 2. Make a program which executes following operations:
    #       a. add x: add x to S
    #       b. remove x: remove x from S
    #                       if there's no x in S, ignore it
    #       c. check x: if x is in S, print 1 else 0
    #       d. toggle x: if x is in S, remove x or vice versa
    #       e. all: change S to {1, 2, 3, ... , 20}
    #       f. empty: clear S

    # Constraints
    # TIME 1500ms
    # SPACE 4MB
    # 1. 1 <= M <= 3 * 10^6
    # 2. 1 <= x <= 20

    # Approach
    # 1. A simple implementation problem with tight constraints.
    # 2. This can be solved with typical int class,
    #       bitmasking is more effecient in terms of memory usage due to the limited range of set.
    # 3. mask = 0
    # 4. add: mask |= (1 << x)
    #    remove: mask &= ~(1 << x)
    #    check: print(1 if (mask & (1 << x)) else 0)
    #    toggle: mask ^= (1 << x)
    #    all: mask = (1 << 20) - 1
    #    empty: mask = 0
    # 5. After writing the psuedo-code, it's clear that the logic required for this problem is bitmasking.

    bitmask = Bitmask()
    m = int(input())
    for _ in range(m):
        _input = input().split()
        if len(_input) == 1:
            bitmask.exec(_input[0])
        else:
            x = int(_input[1]) - 1
            bitmask.exec(_input[0], x)
