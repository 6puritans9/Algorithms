import sys

input = sys.stdin.readline


def max_routes(n: int, grid: list[tuple[int, ...]]) -> int:
    # TC = O(N^2) = O(10^2) < 1000ms
    # SC = O(N^2)

    dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1  # Do not care the starting point of the pipe

    for y in range(n):
        for x in range(n):
            if grid[y][x]:
                continue

            if x > 0:
                dp[y][x][0] += dp[y][x - 1][0]
                dp[y][x][0] += dp[y][x - 1][2]

            if y > 0:
                dp[y][x][1] += dp[y - 1][x][1]
                dp[y][x][1] += dp[y - 1][x][2]

            if y > 0 and x > 0:
                if not grid[y - 1][x] and not grid[y][x - 1]:
                    dp[y][x][2] += dp[y - 1][x - 1][0]
                    dp[y][x][2] += dp[y - 1][x - 1][1]
                    dp[y][x][2] += dp[y - 1][x - 1][2]

    return sum(dp[n - 1][n - 1])


if __name__ == "__main__":
    # 1. An 1-based N*N sized grid is given.
    # 2. Each cell can have 2 states:
    #       0 for blank, 1 for wall.
    # 3. The goal is to bring a pipe from (1,1) to (n, n)
    # 4. It occupies two cells (1,1), (1,2),
    #       and can rotate while moving into three directions:
    #       horizontal, vertical, and diagonal from top-left to bottom-right.
    # 5. If diagonal, it takes 4 cells.
    # 6. It should be rotated by 45 degrees,
    #       and only moves to right or downward,
    #       while it doesn't go over the grid.
    # 7. Find the number of possible routes.
    #       if not possible, return 0.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 3 <= N <= 16
    # 2. 0 <= routes <= 10^6

    # Approach
    # 1. Begin from (0,0), (0,1).
    # 2. The pipe can have 3 states:
    #       a. horizontal
    #       b. diagonal
    #       c. vertical
    # 3. For 'a', two options are available: (y,x+1), (y,x+1) or (y,x+1), (y+1,x+1)
    #   for 'c': (y+1,x), (y+1,x) or (y+1,x), (y+1,x+1)
    #   for 'b', three options: (y+1,x+1), (y,x+1) or (y+1,x+1), (y+1,x) or (y+1,x+1), (y+1,x+1)
    # 4. These states can be divided into steps, which lead to dp.
    # 5. dp[i][j][k] represents number of routes that can be achieved at grid[i][j], having [k] direction.
    # 6. k = 0 | 1 | 2
    #       0 = 'h', 1 = 'v', 2 = 'd'
    # 7. dp[0][0][0] = 1
    #    dp[0][0][1] = 0
    #    dp[0][0][2] = 0
    # 8. if not grid[ny][nx]:
    #       dp[ny][nx][0] = max(dp[ny][nx][0], dp[y][x][0] + dp[y-1][x-1][2])
    #       dp[ny][nx][1] = max(dp[ny][nx][1], dp[y][x][0] + dp[y-1][x-1][2])
    #       dp[ny][nx][2] = max(dp[ny][nx][2], dp[y][x][0] + dp[y-1][x-1][2], dp[y-1][x-1])
    # 9. return sum(dp[n-1][n-1])

    n = int(input())
    grid = []
    for _ in range(n):
        line = tuple(int(num) for num in input().split())
        grid.append(line)
    print(max_routes(n, grid))
