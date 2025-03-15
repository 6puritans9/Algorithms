import sys


def get_input():
    return sys.stdin.readline().rstrip()


def zip(_string):
    result = ""

    for char in _string:
        if not result or char != result[-1]:
            result += char

    return result


if __name__ == "__main__":
    N = int(get_input())
    strings = []
    for i in range(N):
        strings.append(get_input())

    for _string in strings:
        print(zip(_string))
