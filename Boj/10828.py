import sys
from collections import deque


def get_input():
    return sys.stdin.readline().rstrip()


def stack(my_deque, instruction, value=None):
    if instruction == "push":
        my_deque.appendleft(value)
        return None
    elif instruction[0] == "pop":
        if not len(my_deque):
            return -1
        return my_deque.popleft()
    elif instruction[0] == "top":
        if not len(my_deque):
            return -1
        return my_deque[0]
    elif instruction[0] == "size":
        return len(my_deque)
    else:
        if len(my_deque):
            return 0
        return 1



if __name__ == "__main__":
    n = int(get_input())
    s = deque()

    for i in range(n):
        user_input = get_input().split()
        if len(user_input) > 1:
            instruction, value = user_input
            stack(s, instruction, int(value))
        else:
            instruction = user_input
            print(stack(s, instruction))
