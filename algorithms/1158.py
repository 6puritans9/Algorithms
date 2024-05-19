import sys
from collections import deque


def get_input():
    return sys.stdin.readline().rstrip()


def execute(size, steps, people):
    result = deque()
    TURN = steps - 1
    while len(people):
        for i in range(TURN):
            people.append(people.popleft())
        result.append(people.popleft())

    return result


if __name__ == "__main__":
    N, K = [int(num) for num in get_input().split()]
    people = deque(range(1, N + 1))

    result = execute(N, K, people)
    print("<", end="")
    for idx, person in enumerate(result):
        if idx == N - 1:
            print(person, end="")
            break
        print(person, end=", ")
    print(">", end="")
