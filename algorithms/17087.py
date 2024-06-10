import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_answer(N, S, points):
    distances = [abs(S - point) for point in points]
    diff = max(distances)

    if N == 1:
        return diff

    for i, distance in enumerate(distances):
        while distance % diff:
            temp = diff
            diff = distance % diff
            distance = temp

    return diff


if __name__ == "__main__":
    N, S = [int(num) for num in get_input().split()]
    points = sorted(int(num) for num in get_input().split())

    print(get_answer(N, S, points))
