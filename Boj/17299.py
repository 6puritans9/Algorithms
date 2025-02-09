import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(get_input())
    sequence = [int(num) for num in get_input().split()]
    recurrence = [0] * 1000001

    indices = []
    result = [-1] * N

    for number in sequence:
        recurrence[number] += 1

    for i in range(N - 1, -1, -1):
        while indices:
            if recurrence[sequence[i]] >= recurrence[sequence[indices[-1]]]:
                indices.pop()
            else:
                result[i] = sequence[indices[-1]]
                break

        indices.append(i)

    for n in result:
        print(n, end=" ")
