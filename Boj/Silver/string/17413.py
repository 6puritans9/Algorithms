import sys
from collections import deque


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    string = get_input()
    length = len(string)
    d = deque()

    for i, letter in enumerate(string):
        d.append(letter)
        if letter == ">":
            while len(d):
                print(d.popleft(), end="")
        if i + 1 < length and string[i + 1] == "<" and len(d):
            while len(d):
                print(d.pop(), end="")
        elif letter == " " and d[0] != "<":
            d.pop()
            while len(d):
                print(d.pop(), end="")
            print(" ", end="")
        elif i == length - 1:
            while len(d):
                print(d.pop(), end="")
