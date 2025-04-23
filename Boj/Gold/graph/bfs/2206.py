import sys
from collections import deque

input = sys.stdin.readline


def in_range(y, x, rows, cols) -> bool:
    return 0 <= y < rows and 0 <= x < cols


def find_shortest_path(rows: int, cols: int, grid: list[list[int]]) -> int:
    # TC = O(2 states * 4 directions * NM) = O(NM) = O(10^6) < 2000ms
    # SC = O(2 states * bool * NM) = O(NM) = O(2 * 1byte * 10^3 * 10^3) = 2MB

    global GOAL

    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    queue = deque([(0, 0, 1, False)])
    vstd = [[[False, False] for _ in range(cols)] for _ in range(rows)]

    while queue:
        cy, cx, moves, removed = queue.popleft()
        if (cy, cx) == GOAL:
            return moves

        if vstd[cy][cx][removed]:
            continue
        vstd[cy][cx][removed] = True

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx

            if in_range(ny, nx, rows, cols) and not vstd[ny][nx][removed]:
                # wall
                if grid[ny][nx] and not removed:
                    queue.append((ny, nx, moves + 1, True))
                    continue

                # path
                if not grid[ny][nx]:
                    queue.append((ny, nx, moves + 1, removed))

    return - 1


if __name__ == "__main__":
    # 1. An N*M matrix is given.
    # 2. Tile 0 is passable, while 1 stands for a wall.
    # 3. The goal is to find the shortest path to (n,m) from (1,1).
    #       shortest path includes both the starting point and the destination.
    # 4. It is possible to remove a wall to make a new shortest path.
    # 5. You can move in 4 directions, and (1, 1) and (N, M) is always passable.
    # 6. Print the move count of the shortest path or -1 if the destination is unreachable.

    # Constraints
    # TIME 2000ms
    # SPACE 192MB
    # 1. 1 <= N <= 10^3
    # 2. 1 <= M <= 10^3

    # Approach
    # 1. BFS seems feasible.
    # 2. There are two states: Move counts with a wall removed or not.
    #                           queue = [(y, x, moves, removed)]
    # 3. Manage the state with visited list. O(NM) = O(10^3 * 10^3 * 1byte * 2 state) = 2MB
    # 4. return moves if (y, x) == (n-1, m-1) else -1

    n, m = map(int, input().split())
    GOAL = (n - 1, m - 1)
    grid = [[int(num) for num in input().rstrip()] for _ in range(n)]

    print(find_shortest_path(n, m, grid))
