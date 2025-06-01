import sys

input = sys.stdin.readline


# Incorrect
# def dfs(grid: list[tuple[str, ...]], visited: list[list[bool]], in_cycle: list[list[bool]], r: int, c: int) -> int:
#     if visited[r][c] and in_cycle[r][c]:  # existing cycle
#         return 0
#     if visited[r][c] and not in_cycle[r][c]:  # new cycle
#         return 1
#
#     visited[r][c] = True
#
#     direction = grid[r][c]
#     nr, nc = r, c
#     if direction == "D":
#         nr += 1
#     elif direction == "L":
#         nc -= 1
#     elif direction == "R":
#         nc += 1
#     else:
#         nr -= 1
#
#     new_cycle = dfs(grid, visited, in_cycle, nr, nc)
#     if new_cycle:
#         in_cycle[r][c] = True
#
#     return new_cycle

def dfs(grid: list[tuple[str, ...]], visited: list[list[int]], r: int, c: int) -> int:
    if visited[r][c] == 2:  # already fully processed
        return 0
    if visited[r][c] == 1:  # new cycle detected
        return 1

    visited[r][c] = 1

    direction = grid[r][c]
    nr, nc = r, c
    if direction == "D":
        nr += 1
    elif direction == "L":
        nc -= 1
    elif direction == "R":
        nc += 1
    else:
        nr -= 1

    new_cycle = dfs(grid, visited, nr, nc)
    visited[r][c] = 2

    return new_cycle


def min_safe_zones(rows: int, cols: int, grid: list[tuple[str, ...]]) -> int:
    # TC = O(NM) due to visit check
    # SC = O(NM)

    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    safe_zones = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                safe_zones += dfs(grid, visited, r, c)

    return safe_zones


if __name__ == "__main__":
    # 1. An N*M sized grid is given.
    # 2. Each cell has one of 4 directions: down, left, right, up.
    # 3. The goal is to set safe zones that can be approached from anywhere in the grid.
    # 4. Find the possible minimum count of safe zones.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= N <= 10^3
    # 2. 1 <= M <= 10^3
    # 3. No given direction leads to out of bounds.

    # Approach
    # 1. Naive backtracking with visited check will take O(N^2 * N^2).
    # 2. This one requires finding cycle.
    # 3. The distinct number of cycles is the minimum count of safe zones.
    # 4. DFS with 2-layer check is not valid because:
    #       If you mark a node as "visited" as soon as you first visit it, and then revisit it later,
    #       you don’t know if that node is on your current path or not.
    #       a. You found a cycle (came back to a node in the current path), or
    #       b. You’re revisiting a node already explored fully (no cycle here).
    # 5. So (unvisited, visiting, visited) 3 states are crucial to correctly solve the problem.

    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = tuple(char for char in input().rstrip())
        grid.append(row)
    print(min_safe_zones(n, m, grid))
