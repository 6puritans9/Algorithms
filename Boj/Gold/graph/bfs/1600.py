import sys
from collections import deque

input = sys.stdin.readline


def in_range(y, x, w, h) -> bool:
    return 0 <= y < h and 0 <= x < w


def find_min_moves(k: int, w: int, h: int, grid: list[list[int]]) -> int:
    # TC = O(W*H*(K+1))
    # SC = O(W*H*K)
    GOAL = (h - 1, w - 1)

    dys = [-1, 0, 1, 0]
    dxs = [0, -1, 0, 1]
    j_dys = [-2, -2, -1, -1, 1, 1, 2, 2]
    j_dxs = [-1, 1, -2, 2, -2, 2, -1, 1]

    visited = [[[False for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
    queue = deque([(0, 0, k, 0)])  # y, x, remaining k, moves
    while queue:
        cy, cx, ck, moves = queue.popleft()
        if (cy, cx) == GOAL:
            return moves

        if visited[cy][cx][ck]:
            continue
        visited[cy][cx][ck] = True

        # walk
        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx
            if in_range(ny, nx, w, h) and not visited[ny][nx][ck] and not grid[ny][nx]:
                queue.append((ny, nx, ck, moves + 1))

        # jump
        if ck > 0:
            for j_dy, j_dx in zip(j_dys, j_dxs):
                ny, nx = cy + j_dy, cx + j_dx
                if in_range(ny, nx, w, h) and not visited[ny][nx][ck - 1] and not grid[ny][nx]:
                    queue.append((ny, nx, ck - 1, moves + 1))

    return -1


if __name__ == "__main__":
    # Problem
    # Monkey M moves from (0,0) to (H-1, W-1)
    # There are two type of tiles: 0 for ground, 1 for obstacle

    # M basically proceeds to (-1,0), (0,-1), (1,0), (0,1) directions
    # M also jumps like a chess knight for K times
    #   if it jumps, it can move through obstacles
    # Find the minumum count of moves
    #   or not reachable, return -1

    # Constraints
    # 1 <= W, H <= 200 (W, H are natural numbers)
    # 0 <= K <= 30
    # Time 2000ms
    # Space 256MB

    # Approach
    # 1. The most intuitive solution is BFS
    #   it will take O(W*H*(K+1)) time = O(200 * 200 * (30)) = O(1.2 * 10^6) == 6/8 * 1.2 ms
    # 2. Start from (0,0), proceed using dy, dx
    # 3. if (y, x) == (h-1, w-1):
    #       break
    # 4. return min_count which will be the first count of the loop
    # 5. boolean visited array is needed O(W*H*(K+1)) = O(200 * 200* (30)) = 1,200,000 bytes == 1.2MB

    k = int(input())
    w, h = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(h)]

    print(find_min_moves(k, w, h, grid))
