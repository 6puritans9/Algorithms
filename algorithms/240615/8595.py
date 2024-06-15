import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(get_input())
    _str = [char for char in get_input()]

    _sum = 0
    num = ""
    for char in _str:
        if 48 <= ord(char) <= 57:
            num += char
        elif num != "":
            _sum += int(num, 10)
            num = ""

    if num:
        _sum += int(num, 10)

    print(_sum)
