import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(get_input())
    _str = [num for num in get_input()]

    result = 0
    for char in _str:
        result += int(char)
    print(result)
