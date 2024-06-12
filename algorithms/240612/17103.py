import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_table():
    limit = 1000001
    table = [1] * limit
    table[0] = table[1] = 0

    for i in range(2, limit):
        if i*i > limit:
            break
        if table[i]:
            for j in range(i*i, limit, i):
                table[j] = 0

    return table


def get_partitions(table, num):
    count = 0

    for i in range(2, num + 1):
        if i * 2 > num:
            break
        if table[i] and table[num - i]:
            count += 1

    return count


if __name__ == "__main__":
    numbers = []
    prime_table = get_table()

    T = int(get_input())
    for _ in range(T):
        num = int(get_input())
        print(get_partitions(prime_table, num))
