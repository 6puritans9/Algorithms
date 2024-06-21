def get_intersect_count(n, m, list_a, list_b):
    if not n or not m:
        return 0

    intersection = 0
    i = 0
    j = 0

    while i < n and j < m:
        if list_a[i] > list_b[j]:
            j += 1
        elif list_a[i] < list_b[j]:
            i += 1
        else:
            intersection += 1
            i += 1
            j += 1

    return intersection


if __name__ == "__main__":
    N, M = [int(num) for num in input().split()]
    A = [int(num) for num in input().split()]
    B = [int(num) for num in input().split()]

    A.sort()
    B.sort()

    intersection = get_intersect_count(N, M, A, B)
    print(N + M - (intersection * 2))
