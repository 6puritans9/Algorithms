import sys

input = sys.stdin.readline


def find_total_min_cost(n: int, costs: list[tuple[int, int, int]]) -> int:
    # TC = O(N)
    # SC = O(N)

    dp = [[0 for _ in range(3)] for _ in range(n)]

    r, g, b = costs[0]
    dp[0] = [r, g, b]

    for i in range(1, n):
        dp[i] = [costs[i][0] + min(dp[i - 1][1], dp[i - 1][2]), costs[i][1] + min(dp[i - 1][0], dp[i - 1][2]),
                 costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])]

    return min(dp[n - 1])  # every cost is larger than 0


if __name__ == "__main__":
    # There are N houses start from 1 to N.
    # Each house should be painted in either red, blue or green.
    # And house i(2 <= i <= N-1) has to be different from i-1 and i+1
    # As the cost of painting each color is given for N times,
    # Find the total minimum cost.

    # Constraints
    # TIME 500ms
    # SPACE 128MB
    # 1. 2 <= N <= 10^3
    # 2. 0 < cost <= 10^3

    # Approach
    # 1. It appears to be a DP problem.
    # 2. Neighbours have to have distinct colors
    # 3. Create a two-dimensional array which stacks the costs of [r,g,b]

    # 1. dp[0] = [26, 40, 83]
    # 2. dp[1] = [49 + min(dp[0][1], dp[0][2]), 60 + min(dp[0][0], dp[0][2]), 57 + min(dp[0][0], dp[0][1])]
    # 3. dp[i] = [costs[i][0] + min(dp[i-1][1], dp[i-1][2]), costs[i][1] + min(dp[i-1][0], dp[i-1][2]),
    #               costs[i][2] + min(dp[i-1][0], dp[i-1][1])]
    # 4. TC will be O(N) = O(10^3) < 500ms
    # 5. SC will be O(N) = 4bytes * 3 * N = 12bytes * 10^3 = 12KB

    n = int(input())
    costs = []
    for _ in range(n):
        r, g, b = map(int, input().split())
        costs.append((r, g, b))

    print(find_total_min_cost(n, costs))
