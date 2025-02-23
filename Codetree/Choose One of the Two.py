def get_max_sum(n, cards) -> int:
    # dp[i][j] represents the maximum sum when considering the first i cards,
    # while selecting j red cards.
    # j can only go up to n, so it will be (2n + 1) * (n + 1) array with padding.
    dp = [[-1 for _ in range(n + 1)] for _ in range(2 * n + 1)]
    dp[0][0] = 0

    for i in range(1, 2 * n + 1):
        r, b = cards[i]

        for r_count in range(n + 1):
            # The key challange is deciding how to update each state.

            # choose the red card
            if r_count > 0:
                dp[i][r_count] = max(dp[i][r_count], dp[i - 1][r_count - 1] + r)
            # choose the blue card
            if i - r_count > 0:
                dp[i][r_count] = max(dp[i][r_count], dp[i - 1][r_count] + b)

    # The answer is the last element of the dp table,
    # which represents for the maximum sum achievable after considering all the card sets
    # with n red card selected.
    return dp[2 * n][n]


if __name__ == "__main__":
    n = int(input())
    cards = [0, *(tuple(map(int, input().split())) for _ in range(n * 2))]

    print(get_max_sum(n, cards))
