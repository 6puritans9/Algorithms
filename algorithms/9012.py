import sys
from collections import deque


def get_input():
    return sys.stdin.readline().rstrip()


def validate(string):
    stack = deque()

    for idx, letter in enumerate(string):
        length = len(string)
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if not len(stack) or stack.pop() != "(":
                return "NO"
        if idx == length -1 and len(stack):
            return "NO"
    return "YES"


if __name__ == "__main__":
    T = int(get_input())
    strings = []
    for _ in range(T):
        strings.append(get_input())

    for string in strings:
        print(validate(string))

