import sys

print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def verify_sequence(inputs, numbers_length):
    result = []
    stack = []

    current = 1
    for input in inputs:
        while current <= input:
            stack.append(current)
            result.append("+")
            current += 1

        if stack[-1] == input:
            stack.pop()
            result.append("-")
        else:
            return "NO"

    return result


if __name__ == "__main__":
    n = int(get_input())
    inputs = [0] * n
    for i in range(n):
        inputs[i] = (int(get_input()))

    result = verify_sequence(inputs, n)

    if type(result) is str:
        print(result)
    else:
        for letter in result:
            print(f"{letter}\n")
