# This one is a minor tweak of previous knapsack problem.
# While the previous one didn't allow the use of same element multiple times,
# this one allows the same element to be used multiple times.
# Which is more straightforward to implement by iterating from 1 to n.
# Only took less than 10 minutes to solve this problem! Love it!🥰

def get_max_profit(profits, n):
    dp = [-1] * (n + 1)
    dp[0] = 0

    for length, profit in enumerate(profits):
        for i in range(1, n+1):
            if length <= i and dp[i-length] != -1:
                dp[i] = max(dp[i], dp[i - length] + profit)

    return max(dp)


if __name__ == "__main__":
    n = int(input())
    profits = [0] + list(map(int, input().split()))
    profits = tuple(profits)

    print(get_max_profit(profits, n))


# It can get a little space optimization(17MB >> 16MB)
# and better readability with writing as follows:

# def get_max_profit(profits, n):
#     dp = [0] * (n + 1)
#
#     for length, profit in enumerate(profits):
#         for i in range(length, n+1):
#                 dp[i] = max(dp[i], dp[i - length] + profit)
#
#     return max(dp)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     profits = (0, *map(int, input().split()))
#
#     print(get_max_profit(profits, n))
