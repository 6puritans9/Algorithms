import sys

input = sys.stdin.readline


def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def find_paths(n: int, grid: list[list[int]]) -> int:
    # TC = O(N^2)
    # SC = O(N^2)

    # dp[i][j] = considering grid[i][j], the number of paths
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1

    for y in range(n):
        for x in range(n):
            if not dp[y][x]:
                continue

            dist = grid[y][x]
            if not dist:
                continue

            if in_range(y, x + dist, n):
                dp[y][x + dist] += dp[y][x]
            if in_range(y + dist, x, n):
                dp[y + dist][x] += dp[y][x]

    return dp[n - 1][n - 1]


if __name__ == "__main__":
    # In N*N sized grid, traverse from (0,0) to (N-1, N-1)
    # grid[i][j] indicates how far it can jump
    # directions must be either right or down
    # if grid[i][j] == 0, it cannot jump further
    # Find the number of paths that can reach (N-1, N-1)

    # 4 <= N <= 100
    # brute force will take O(2^2N), which can have 2^200 in worst case scenario
    # it is way too large to compute, so this approach is not feasible

    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(find_paths(n, grid))
