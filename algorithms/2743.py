import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    _str = get_input()
    print(len(_str))
