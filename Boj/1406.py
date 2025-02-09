import sys
from collections import deque

print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def editor(instruction, value=None):
    global left_stack
    global right_stack

    if instruction == "L":
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif instruction == "D":
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif instruction == "B":
        if len(left_stack):
            left_stack.pop()
    else:
        left_stack.append(value)


if __name__ == "__main__":
    left_stack = deque()
    right_stack = deque()

    for letter in get_input():
        left_stack.append(letter)

    n = int(get_input())
    for _ in range(n):
        instructions = get_input().split()
        if len(instructions) > 1:
            instruction, value = instructions
            editor(instruction, value)
        else:
            instruction = instructions[0]
            editor(instruction)

    left_stack.extend(right_stack)
    sys.stdout.write(''.join(left_stack))
