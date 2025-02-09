import sys
from collections import deque


def get_input():
    return sys.stdin.readline().rstrip()


def calculate(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 / num2


if __name__ == "__main__":
    N = int(get_input())
    _string = deque([char for char in get_input()])
    numbers = deque()
    CHAR_VALUE = 65

    values = [0] * N
    for i in range(N):
        values[i] = int(get_input())

    while _string:
        if _string[0] == '+' or _string[0] == '-' or _string[0] == '*' or _string[0] == '/':
            op = _string.popleft()
            num2 = numbers.pop()
            num1 = numbers.pop()
            numbers.append(calculate(op, num1, num2))
        else:
            numbers.append(values[ord(_string.popleft()) - CHAR_VALUE])

    print(f"{numbers.pop():.2f}")
