import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_result(N, K):
    result = [0]
    f_K = K % 10
    f_K2 = 2*K % 10

    for n in range(1, N + 1):
        if n % 10 == f_K or n % 10 == f_K2:
            continue
        result.append(n)
        result[0] += 1

    return result


if __name__ == "__main__":
    N, K = [int(num) for num in get_input().split()]

    result = get_result(N, K)
    for i, num in enumerate(result):
        if i == 0:
            print(num)
            continue
        if result[0] != 0:
            print(num, end=" ")
        elif result[0] == 0:
            print()
