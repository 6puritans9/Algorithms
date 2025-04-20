import sys

input = sys.stdin.readline


def find_max_subseq_len(n: int, numbers: list[int]) -> int:
    # TC = O(N^2)
    # SC = O(N)

    dp = [1 for _ in range(n)]  # As every element has own length

    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    # For given sequence A,
    # Find the longest increasing subsequence.
    # Subsequence doesn't have to be continuous.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= N <= 10^3
    # 2. 1 <= Ai <= 10^3

    # Approach
    # 1. Nested loop will solve this easily O(10^6)
    # 2. Greedy doesn't find the optimal solution
    #    Edge case:
    #       5
    #       1 10 2 3 4
    # 3. Nest dp will solve this correctly
    # 4. Return max(dp)

    n = int(input())
    numbers = [int(num) for num in input().split()]
    print(find_max_subseq_len(n, numbers))
