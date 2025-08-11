import sys
import bisect

input = sys.stdin.readline


def find_lis(n: int, seq: tuple[int, ...]) -> list[int]:
    # TC = O(NlogN)
    # SC  = O(N)

    lis = [seq[0]]
    lis_idx = [0]
    prev = [-1 for _ in range(n)]

    for i in range(1, n):
        cur = seq[i]
        if cur > lis[-1]:
            prev[i] = lis_idx[-1]
            lis.append(cur)
            lis_idx.append(i)
            continue

        pos = bisect.bisect_left(lis, cur)
        lis[pos] = cur
        lis_idx[pos] = i
        if pos > 0:
            prev[i] = lis_idx[pos - 1]

    out = []
    idx = lis_idx[-1]
    while idx != -1:
        out.append(seq[idx])
        idx = prev[idx]
    out.reverse()

    return out


if __name__ == "__main__":
    # 1. N-sized sequence A is given.
    # 2. Find the LIS and print length and the subsequence.

    # Constraints
    # TIME 3000ms
    # SPACE 512MB
    # 1. 1 <= N <= 10^6
    # 2. -10^9 <= Ai <= 10^9

    # Approach
    # 1. dp will take O(N^2) = O(10^12) which takes too long.
    # 2. binary search can reudce it to O(NlogN) == O(10^6) < 3000ms
    # 3. make an empty list LIS, push the first element of the given sequence.
    # 4. from index 1, compare seq[i] to the last element of LIS.
    #       a. if seq[i] > LIS[last], LIS.append(seq[i])
    #       b. else, find the insertion index using bisect.

    n = int(input())
    A = tuple(int(num) for num in input().split())

    result = find_lis(n, A)
    print(len(result))
    print(*result)
