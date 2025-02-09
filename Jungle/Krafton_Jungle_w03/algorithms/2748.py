import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp_table = [0 for _ in range(n)]
    dp_table[0] = 1
    dp_table[1] = 1
    for i in range(2, n):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

    return dp_table[n - 1]


if __name__ == "__main__":
    n = int(get_input())
    print(get_fibonacci(n))
