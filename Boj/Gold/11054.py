import sys

input = sys.stdin.readline


def find_max_bitonic_len(n: int, seq: tuple[int, ...]) -> int:
    # TC = O(N^2)
    # SC = O(2N)

    lis = [1 for _ in range(n)]
    lds = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                lds[i] = max(lds[i], lds[j] + 1)

    max_len = 0
    for i in range(n):
        max_len = max(max_len, lis[i] + lds[i] - 1)  # handle double added peak

    return max_len


if __name__ == "__main__":
    # 1. A sequence 'A' is given.
    # 2. Find the length of the longest subsequence of A, that is a bitonic sequence.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= n <= 10^3
    # 2. 1 <= element <= 10^3

    # Approach
    # 1. A dp problem.
    # 2. Pre-compute LIS and LDS for each index. O(N^2)
    # 3. Find the max(LIS[i] + LDS[i])

    n = int(input())
    A = tuple(int(num) for num in input().split())
    print(find_max_bitonic_len(n, A))
