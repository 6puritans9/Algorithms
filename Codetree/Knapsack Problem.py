def get_max_value(n, jewels, m) -> int:
    dp = [-1] * (m + 1)
    dp[0] = 0

    for weight, value in jewels:
        if weight > m:
            break

        for i in range(m, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + value)

    return max(dp)


if __name__ == "__main__":
    n, m = map(int, input().split())
    jewels = [tuple(map(int, input().split())) for _ in range(n)]
    jewels.sort()

    print(get_max_value(n, jewels, m))

# My first solution was as follows, which had 3 problems.
# 1. It didn't take the optimal value for each weight in dp[i], not using max() which led to unexpected results.
# 2. This approach cannot handle the case where the weight is duplicated.
#   - this issue took me the longest to figure out.
# 3. The order of nested loop had to be reversed to make it work properly.

# def get_max_value(n, jewels, m) -> int:
#     dp = [-1] * (m + 1)
#     dp[0] = 0
#
#     for i in range(1, m + 1):
#         for weight, value in jewels:
#             if weight > m:
#                 break
#             if i - weight >= 0 and dp[i-weight] != -1:
#                 if i-weight == weight:
#                     continue
#                 dp[i] = dp[i-weight] + value
#
#     return max(dp)
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     jewels = [tuple(map(int, input().split())) for _ in range(n)]
#     jewels.sort()
#
#     print(get_max_value(n, jewels, m))

# So the correction was made as follows:
# 1. Use max() to compare the optimal state for each step in dp[i]
# 2. Use the reversed order of nested loop to handle the case where the weight is duplicated.
#
# This one is a classic knapsack problem, which can be also solved with two-dimensional dp.
# The time complexity is same O(NM) for both cases, but this one is more space efficient,
# because it only uses one-dimensional dp(O(N+M), N for input, M for dp).
