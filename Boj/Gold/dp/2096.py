import sys

input = sys.stdin.readline


def in_range(x: int) -> bool:
    return 0 <= x < 3


def find_min_max(n: int, grid: list[tuple[int, ...]]) -> tuple[int, int]:
    # TC = O(N)
    # SC = O(1)

    prv_min = list(grid[0])
    prv_max = list(grid[0])

    for r in range(1, n):
        cur_min = [float("inf") for _ in range(3)]
        cur_max = [-1 for _ in range(3)]

        for c in range(3):
            for nc in range(c - 1, c + 2):
                if in_range(nc):
                    cur_min[c] = min(cur_min[c], prv_min[nc] + grid[r][c])
                    cur_max[c] = max(cur_max[c], prv_max[nc] + grid[r][c])
        prv_min, prv_max = cur_min, cur_max

    return max(prv_max), min(prv_min)


if __name__ == "__main__":
    # 1. There are N rows that have 3 cols.
    # 2. Each col can have a number range from (0, 10)
    # 3. Starting from row 0, descend to row n-1.
    # 4. The number in the same col or the neighbouring col can be earned.
    # 5. Find the maximum achievable score and the minimum.

    # Constraints
    # TIME 1000ms
    # SPACE 4MB
    # 1. 1 <= N <= 10^5

    # Approach
    # 1. This is a dp problem that should handle both cases individually.
    # 2. Initialize the dp table with grid[0]
    # 3. From row 1, add the current possible value to the previous dp value.
    # 4. Store the min or max value in the dp table.
    # 5. Because of the tight memory limit, O(1) space complexity is required.

    n = int(input())
    grid = [tuple(int(num) for num in input().split()) for _ in range(n)]
    result = find_min_max(n, grid)
    print(" ".join(map(str, result)))
