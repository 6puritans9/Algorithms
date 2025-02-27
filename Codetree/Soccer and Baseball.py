# I'm getting the grasp of it!

def find_max_sum(n, f, b):
    # dp[i][j][k] = max sum using first i students with j football and k baseball players
    dp = [[[-1 for _ in range(10)] for _ in range(12)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        for j in range(11, -1, -1):
            for k in range(9, -1, -1):
                if dp[i - 1][j][k] == -1:
                    continue

                football, baseball = f[i], b[i]
                if j < 11:
                    dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i - 1][j][k] + football)
                if k < 9:
                    dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i - 1][j][k] + baseball)

                # when skip current player
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])

    return dp[n][11][9]


if __name__ == "__main__":
    n = int(input())
    football, baseball = [0], [0]

    for _ in range(n):
        f, b = map(int, input().split())
        football.append(f)
        baseball.append(b)

    print(find_max_sum(n, football, baseball))
