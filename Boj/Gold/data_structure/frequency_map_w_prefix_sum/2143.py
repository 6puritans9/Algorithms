import sys
from collections import defaultdict

input = sys.stdin.readline


def get_prefix_sum(length: int, array: list[int]) -> dict[int, int]:
    # TC = O(N^2) + O(M^2) == O(N^2)
    # SC = O(N)

    prefix_sum = defaultdict(int)

    for i in range(length):
        current_sum = 0

        for j in range(i, length):
            current_sum += array[j]
            prefix_sum[current_sum] += 1

    return prefix_sum


def find_possible_subarrays(t: int, prefix_a: dict[int, int], prefix_b: dict[int, int]) -> int:
    # TC = O(len(prefix_b))
    # SC = O(1)

    count = 0

    for b in prefix_b:
        complement = t - b
        if complement in prefix_a:
            count += prefix_a[complement] * prefix_b[b]

    return count


if __name__ == "__main__":
    # 1. Two arrays are given.
    # 2. For the subarrays of each given array,
    # 3. Find the subarrays that the sum makes T.
    # 4. Print 0 if not possible.

    # Constraints
    # TIME 2000ms
    # SPACE 64MB
    # 1. -10^9 <= T <= 10^9
    # 2. 1 <= N <= 10^3
    # 3. 1 <= M <= 10^3
    # 4. -10^6 <= element <= 10^6

    # Approach
    # 1. The most intuitive solution is nested loop of possible subarrays O(N^2 * M^2) = O(10^12),
    #       which will easily be over the time limit.
    # 2. Therefore, the solution should take something like O(NM) = O(10^6).

    # 3. Compute all the possible prefix sum. O(N^2 + M^2)
    # 4. For one of the prefix sums, iterate it
    #       and find if (t - element) exists in the other side. O(NM)
    # 5. The total time complexity is O(N^2 + M^2) + O(NM) == O(N^2) = O(10^6) < 2000ms
    # 6. Return the count.

    t = int(input())
    n = int(input())
    A = [int(num) for num in input().split()]
    m = int(input())
    B = [int(num) for num in input().split()]

    prefix_sum_a = get_prefix_sum(n, A)
    prefix_sum_b = get_prefix_sum(m, B)

    print(find_possible_subarrays(t, prefix_sum_a, prefix_sum_b))
