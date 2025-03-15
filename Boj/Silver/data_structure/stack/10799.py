import sys


def get_input():
    return sys.stdin.readline().rstrip()


def count_pieces(_str):
    length = len(_str)
    bars = 0
    pieces = 0

    for i, p in enumerate(_str):
        if p == "(":
            if i+1 < length and _str[i+1] == ")":
                # cutter
                pieces += bars
            else:
                bars += 1
                pieces += 1
        else:
            if i - 1 > 0 and _str[i-1] != "(":
                bars -= 1

    return pieces


if __name__ == "__main__":
    _input = [letter for letter in input()]
    print(count_pieces(_input))
