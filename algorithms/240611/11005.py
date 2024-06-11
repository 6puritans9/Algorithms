import sys
from collections import deque
print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def convert(num, base):
    result = deque()

    while num > 0:
        remain = num % base
        if remain > 9:
            result.appendleft(chr(65 + (remain - 10)))
        else:
            result.appendleft(remain)
        num //= base

    return result


if __name__ == "__main__":
    N, B = [int(num) for num in get_input().split()]

    result = convert(N, B)
    for letter in result:
        print(str(letter))
