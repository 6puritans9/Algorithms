import sys


def get_input():
    return sys.stdin.readline().rstrip()


def count_zeroes(N):
    result = [0, 0]

    for n in range(N + 1):
        if n == 0 or n == 1:
            continue

        while n % 2 == 0 or n % 5 == 0:
            if n % 2 == 0:
                result[0] += 1
                n //= 2
            else:
                result[1] += 1
                n //= 5

    return result


if __name__ == "__main__":
    N = int(get_input())

    result = count_zeroes(N)

    if not result[0] or not result[1]:
        print(0)
    else:
        print(min(result))
