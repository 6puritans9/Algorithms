import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_section(level):
    if level == 300:
        return 1
    elif 275 <= level < 300:
        return 2
    elif 250 <= level < 275:
        return 3
    else:
        return 4


if __name__ == "__main__":
    N = int(get_input())
    levels = [int(num) for num in get_input().split()]

    for level in levels:
        print(get_section(level), end=" ")
