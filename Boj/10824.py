import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    strings = [num for num in get_input().split()]
    a, b, c, d = strings
    result = [int(a+b), int(c+d)]

    print(sum(result))
