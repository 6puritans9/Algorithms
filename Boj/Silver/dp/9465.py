import sys

input = sys.stdin.readline


def find_max_score(n: int, stickers: list[tuple[int, ...]]) -> int:
    # TC = O(N) = O(10^5) < 1000ms
    # SC = O(N) = 4bytes * 2 * 10^5 = 800KB

    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    dp[1][0], dp[1][1] = stickers[0][0], stickers[0][1]

    for i in range(2, n + 1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 2][0], dp[i - 2][1]) + stickers[i - 1][0]
        dp[i][1] = max(dp[i - 1][0], dp[i - 2][0], dp[i - 2][1]) + stickers[i - 1][1]

    return max(dp[n])


if __name__ == "__main__":
    # 1. A (2 * n) list is given.
    # 2. Each cell has score.
    # 3. If a cell is selected, it's adjacent cell becomes unavailable to select.
    # 4. Find the maximum sum of selected scores.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= n <= 10^5
    # 2. 0 <= score <= 10^2

    # Approach
    # 1. This is a dp problem
    # 2. Each cell can have two states: be selected or not
    # 3. Create a dp[2][n+1]
    # 4. Initialize dp[0][0], dp[0][1] = 0, 0
    #               dp[1][0], dp[1][1] = stickers[0][0], stickers[0][1]
    # 5. dp[i][0] = max(dp[i-1][1], dp[i-2][0], dp[i-2][1]) + stickers[i-1][0] // 0-based
    #    dp[i][1] = max(dp[i-1][0], dp[i-2][0], dp[i-2][1]) + stickers[i-1][1]
    # 6. return max(dp[n])

    t = int(input())
    for _ in range(t):
        n = int(input())
        stickers = []
        row1 = [int(num) for num in input().split()]
        row2 = [int(num) for num in input().split()]
        for i in range(n):
            stickers.append((row1[i], row2[i]))

        print(find_max_score(n, stickers))
