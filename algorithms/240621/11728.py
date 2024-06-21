import sys


def get_input():
    return sys.stdin.readline().rstrip()


def concat(n, m, list_a, list_b):
    result = []
    i = 0
    j = 0

    while i < n and j < m:
        if list_a[i] > list_b[j]:
            result.append(list_b[j])
            j += 1
        elif list_a[i] <= list_b[j]:
            result.append(list_a[i])
            i += 1
        # else:
        #     result.append(list_a[i])
        #     i += 1
        #     j += 1

    while i < n:
        result.append(list_a[i])
        i += 1

    while j < m:
        result.append(list_b[j])
        j += 1

    return result


if __name__ == "__main__":
    N, M = [int(num) for num in get_input().split()]
    A = [int(num) for num in get_input().split()]
    B = [int(num) for num in get_input().split()]

    result = concat(N, M, A, B)
    length = len(result)

    for i, num in enumerate(result):
        if i == length - 1:
            break
        print(num, end=" ")

    print(result[length - 1])
