import sys
from collections import deque
# print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


class Queue:
    def __init__(self):
        self.q = deque()

    def empty(self):
        if len(self.q):
            return 0

        return 1

    def size(self):
        return len(self.q)

    def front(self):
        if self.empty():
            return -1

        return self.q[0]

    def back(self):
        if self.empty():
            return -1

        return self.q[-1]

    def push(self, value):
        self.q.append(value)

    def pop(self):
        if self.empty():
            return -1

        return self.q.popleft()


if __name__ == "__main__":
    N = int(get_input())
    inputs = []

    for i in range(N):
        _input = get_input().split()
        if len(_input) == 1:
            inputs.append(_input)
        else:
            instruction, value = _input
            inputs.append([instruction, int(value)])

    q = Queue()

    for input in inputs:
        if len(input) > 1:
            q.push(input[1])
        elif input[0] == "pop":
            print(q.pop())
        elif input[0] == "size":
            print(q.size())
        elif input[0] == "empty":
            print(q.empty())
        elif input[0] == "front":
            print(q.front())
        else:
            print(q.back())

