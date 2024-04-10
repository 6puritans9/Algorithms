import sys


def get_input():
    return sys.stdin.readline().rstrip()


def check_have_cross(table, row, col):
    if sum(table[row]) > 1 or sum(table[col]) > 1:
        return True


def check_have_diagonal(table, coord):



def get_count(table, n, i, j):
    if i >= n or j >= n:
        return 0
    elif check_have_cross(table, i, j):
        return 0
    elif check_have_diagonal(table, [i, j]):
        return 0

    table[i][j] = 1

    for row in range(i + 1, n):
        for col in range(j + 1, n):
            get_count(table, n, row, col)

    count += get_count(table, n, i + 1, j)


if __name__ == "__main__":
    n = int(get_input())
    table = [[0 for _ in range(n)] for _ in range(n)]
    get_result(table, n, 0, 0)
    print()
