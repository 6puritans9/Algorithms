# Another failed one.
#
# What I've figured:
# 1. Two-dimensional dp table is necessary: one for player one index, one for player two index
# 2. It can be divided into three cases:
#       a. player one drops
#       b. player two drops, gets the point
#       c. both players drop
#
# What I didn't solve:
# 1. Where to start and how to proceed:
#   a. I began to build dp table from index 1 while looking backward, which didn't reduce the complexity at all
#   b. Didn't figure out how index proceeding should be handled.
# 2. Didn't catch how to make dropping both case properly.
#
# So, I'm start to realizing is all about making idea simple.
# Implementing divide and conqure.
#
# And for this problem, it feels recursion with memoization is more natural.

# Tabulation
def get_max_score(n, first_cards, second_cards) -> int:
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue

            first_c = first_cards[i + 1]
            second_c = second_cards[j + 1]

            if second_c < first_c:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + second_c)
            if first_c < second_c:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            # Drop both cards
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

    return max(max(row) for row in dp)


# Memoization
# def dfs(n, first_cards, second_cards, memo, i, j) -> int:
#     if memo[i][j] != -1:
#         return memo[i][j]
#     if i == n or j == n:
#         return 0
#
#     first_c = first_cards[i + 1]
#     second_c = second_cards[j + 1]
#     result = -float("inf")
#
#     if second_c < first_c:
#         result = max(result, dfs(n, first_cards, second_cards, memo, i, j + 1) + second_c)
#     elif first_c < second_c:
#         result = max(result, dfs(n, first_cards, second_cards, memo, i + 1, j))
#     result = max(result, dfs(n, first_cards, second_cards, memo, i + 1, j + 1))
#
#     memo[i][j] = result
#
#     return result
#
#
# def get_max_score(n, first_cards, second_cards) -> int:
#     memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
#
#     return dfs(n, first_cards, second_cards, memo, 0, 0)


if __name__ == "__main__":
    n = int(input())
    first_cards = [0, *(int(num) for num in input().split())]
    second_cards = [0, *(int(num) for num in input().split())]

    print(get_max_score(n, first_cards, second_cards))
