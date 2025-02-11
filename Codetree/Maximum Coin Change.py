def get_max_changes(coins, m) -> int:
    dp = [-1] * (m + 1)
    dp[0] = 0

    for i in range(1, m + 1):
        for coin in coins:
            if coin > m:
                break
            if i >= coin and dp[i - coin] != -1:
                dp[i] = max(dp[i], dp[i - coin] + 1)

    return dp[m]


if __name__ == "__main__":
    n, m = map(int, input().split())
    coins = [int(coin) for coin in input().split()]
    coins.sort()

    print(get_max_changes(coins, m))

# My initial solution was as follows,
# and it was incorrect because it didn't build on the previous state if it was valid
# by checking dp[i-coin] == -1.
# I figured this out by checking the log for the case n, m = 99 7969 case🤣

# def get_max_changes(n, coins, m) -> int:
#     dp = [-1] * (m + 1)
#     dp[0] = 0
#
#     for i in range(1, m+1):
#         for coin in coins:
#             if i >= coin:
#                 dp[i] = max(dp[i], dp[i-coin] + 1)
#
#     return dp[m]
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     coins = [int(coin) for coin in input().split()]
#
#     print(get_max_changes(n, coins, m))
