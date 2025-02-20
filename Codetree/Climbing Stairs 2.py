# Now this one was tricky.
# The constraint was that you can take either 1 step or 2 steps to the top,
# but you can only take up to 3 steps if you take 1 step.

# My idea was valid, but the implementation was wrong.
# What I thought was:
# 1. dp[i][j] means you consider the i-th step with j steps(for single step taken).
# 2. So it needs to be evaluated by the previous state, which is dp[i-1][j-1] + coins[i] or dp[i-2][j] + coins[i].
# 3. You can access every step by taking 1 step, so the dp table should be initialized by 0.
# It worked for simple cases, but didn't last for long😓.

# So, the takeaways are:
# 1. Make sure to set the starting point correctly.
# 2. Make concrete definitions for each state.
# 3. Think of unreachable states and how to handle them.

def get_max_coins(n, coins) -> int:
    MAX_STEPS = 3
    dp = [[-1 for _ in range(MAX_STEPS + 1)] for _ in range(n + 1)]

    dp[1][1] = coins[1]
    dp[2][0] = coins[2]

    for i in range(3, n + 1):
        coin = coins[i]

        for j in range(MAX_STEPS + 1):
            if j > 0 and dp[i - 1][j - 1] != -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin)

            if dp[i - 2][j] != - 1:
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin)

    return max(dp[n])


# Initial implementation

# def get_max_coins(n, coins) -> int:
#     MAX_STEP = 3
#     dp = [[0 for _ in range(MAX_STEP + 1)] for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         coin = coins[i]
#
#         for j in range(1, MAX_STEP + 1):
#             dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin, dp[i-2][j] + coin)
#
#     return dp[n][MAX_STEP]


if __name__ == "__main__":
    n = int(input())
    coins = [0, *(int(num) for num in input().split())]

    print(get_max_coins(n, coins))
