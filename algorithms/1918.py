import sys
from collections import deque

def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    expression = get_input()
    output = deque()
    operators = deque()

    for char in expression:
        if char == "(":
            operators.append(char)
        elif char == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()


            # equal or lower precedence ahead
        elif char in "*/":
            while operators and operators[-1] in "*/":
                output.append(operators.pop())
            operators.append(char)
        # equal or higher precedence ahead
        elif char in "+-":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            operators.append(char)
        # operands
        else:
            output.append(char)

    # append remaining operators
    while operators:
        output.append(operators.pop())

    for char in output:
        print(char, end="")
