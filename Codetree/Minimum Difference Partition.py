# This one was pretty hard to solve for me
# Because the technique using boolean to mark the possibility for each case was unfamiliar to me.
# My approach was restricted to only how to iterate given input numbers,
# which couldn't handle the complexity of the solution.

def get_min_diff(numbers, n) -> int:
    # dp[i][j] = is part_sum j achievable when i was selected

    # [from 0 to maximum limit(TOTAL)] per row
    # row per each number in numbers
    TOTAL = sum(numbers)
    dp = [[False for _ in range(TOTAL + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        # Since number is (0, *input), numbers[i] is the actual i-th number.
        cur_num = numbers[i]

        for part_sum in range(TOTAL + 1):
            # include cur_num
            if dp[i - 1][part_sum - cur_num]:
                dp[i][part_sum] = True
            # If we don't include cur_num, we check if part_sum was already possible without it.
            # If so, part_sum can still be achieved without cur_num.
            elif dp[i - 1][part_sum]:
                dp[i][part_sum] = True
            # And cur_num belongs to the other part.

    # Use brute force to get the minimum difference
    min_diff = float("inf")
    for i in range(TOTAL):
        if dp[n][i]:
            min_diff = min(min_diff, abs(i - (TOTAL - i)))

    return min_diff


if __name__ == "__main__":
    n = int(input())
    numbers = (0, *map(int, input().split()))

    print(get_min_diff(numbers, n))
