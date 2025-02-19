# This one is very straightforward approach.
# Which takes O(N) time complexity and O(N) space complexity.

def find_max_subseq_len(n, numbers) -> int:
    dp = [-float("inf")] * n
    dp[0] = numbers[0]

    for i in range(1, n):
        dp[i] = max(numbers[i], dp[i - 1] + numbers[i])

    return max(dp)


if __name__ == "__main__":
    n = int(input())
    numbers = [int(num) for num in input().split()]

    print(find_max_subseq_len(n, numbers))

# It can be optimized to O(1) space complexity, by using only one variable to store the previous state.
# Which is called Kadane's Algorithm.
# The core idea is to decide whether to extend the previous subarray or start a new one at every step.
#
# def find_max_subseq_len(n, numbers) -> int:
#     max_sum = -float("inf")
#     current_sum = numbers[0]
#
#     for i in range(1, n):
#         current_sum = max(numbers[i], current_sum + numbers[i])
#         max_sum = max(max_sum, current_sum)
#
#     return max_sum
#
#
# if __name__ == "__main__":
#     n = int(input())
#     numbers = [int(num) for num in input().split()]
