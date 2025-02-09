import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(get_input())
    sequence = [int(num) for num in get_input().split()]
    indices = []
    result = [-1] * N

    for i in range(N - 1, -1, -1):
        while indices and sequence[indices[-1]] <= sequence[i]:
            indices.pop()

        if indices:
            result[i] = sequence[indices[-1]]

        indices.append(i)

    for n in result:
        print(n, end=" ")
