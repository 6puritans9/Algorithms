import sys
from collections import deque
print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def get_negabinary(num):
    if num == 0:
        return "0"

    result = deque()
    BASE = -2

    while num != 0:
        remainder = num % BASE
        num //= BASE

        if remainder < 0:
            remainder = abs(remainder)
            num += 1

        result.appendleft(str(remainder))

    return "".join(result)


if __name__ == "__main__":
    N = int(get_input())
    print(get_negabinary(N))
