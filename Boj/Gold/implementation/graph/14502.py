import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def in_range(y, x, r, c) -> bool:
    return 0 <= y < r and 0 <= x < c


def find_candidates(grid, rows: int, cols: int) -> list[tuple[int, int]]:
    candidates = []

    for y in range(rows):
        for x in range(cols):
            if not grid[y][x]:
                candidates.append((y, x))

    return candidates


def count_free_area(grid, rows, cols) -> int:
    count = 0

    for y in range(rows):
        for x in range(cols):
            if not grid[y][x]:
                count += 1

    return count


def spread_virus(src_grid, rows, cols, walls: tuple[tuple[int, int], ...]) -> int:
    # SC = O(NM)

    grid = [row[:] for row in src_grid]
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    # build wall
    for r, c in walls:
        grid[r][c] = 1

    # search for virus
    q = deque()
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 2:
                q.append((y, x))

    while q:
        cy, cx = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx
            if in_range(ny, nx, rows, cols) and not grid[ny][nx]:
                grid[ny][nx] = 2  # infect
                q.append((ny, nx))

    return count_free_area(grid, rows, cols)


def find_max_safe_area(grid, rows: int, cols: int, combs) -> int:
    # TC = O((NM)^4)
    # SC = O(NM)

    max_safe = 0

    for comb in combs:
        max_safe = max(max_safe, spread_virus(grid, rows, cols, comb))

    return max_safe


if __name__ == "__main__":
    # 1. N * M sized grid is given.
    # 2. Each tile can have state of 0, 1, 2.
    #       0 for a blank space
    #       1 for a wall
    #       2 for virus
    # 3. It is possible to build new walls up to 3.
    # 4. Virus can spread to north, south, east, west.
    # 5. Find the maximum number of virus-free tiles after building 3 walls.

    # Constraints
    # SPACE 2000ms
    # TIME 512MB
    # 1. N <= 3
    # 2. M <= 8
    # 3. 2 <= virus <= 10
    # 4. 3 <= blank tile

    # Approach
    # 1. Maximum time for backtracking O(C(blank tiles, 3)* (N * M)) == O((NM)^3 * NM) = O((NM)^4)
    #       = O(24^4) == O(10^4) < 2000ms
    # 2. So this is a backtracking problem for sure.
    # 3. Or, I can make an array of coordinates
    #       which are eligible for building walls O(N).
    # 4. Make combinations of eligible tiles and set walls up.
    # 5. Find and compare the maximum free tiles iterating the grid O(NM).

    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        tiles = [int(num) for num in input().split()]
        grid.append(tiles)

    tiles_for_walls = find_candidates(grid, n, m)
    combs_for_walls = combinations(tiles_for_walls, 3)

    print(find_max_safe_area(grid, n, m, combs_for_walls))
