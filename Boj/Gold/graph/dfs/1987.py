import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]


def in_range(y: int, x: int) -> bool:
    global r, c

    return 0 <= y < r and 0 <= x < c


def dfs(y: int, x: int, grid, mask: int, steps: int) -> int:
    max_steps = steps

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if in_range(ny, nx):
            next_exp = ord(grid[ny][nx]) - ord("A")
            next_mask = mask | (1 << next_exp)

            if not (mask & (1 << next_exp)):
                max_steps = max(max_steps, dfs(ny, nx, grid, next_mask, steps + 1))

    return max_steps


def find_max_steps(grid: tuple[tuple[str, ...], ...]) -> int:
    # TC = O(RC * 2^26)
    # SC = O(RC)

    start_exp = ord(grid[0][0]) - ord("A")
    start_mask = 1 << start_exp

    return dfs(0, 0, grid, start_mask, 1)


if __name__ == "__main__":
    # 1. An R*C board is given.
    # 2. Each tile has an uppercase alphabet.
    #  3. Starting from (0, 0), it can move to neighbouring (N, S, E, W) tile.
    #  4. Because it tracks the alphabet, it cannot step on the same alphabet.
    #  5. Find the maximum number of tiles it can pass through

    #  Constraints
    #  TIME 2000ms
    #  SPACE 256MB
    #  1. 1 <= R, C <= 20

    #  Approach
    #  1. A dfs problem.
    #  2. Store the state in two layers:
    #       [steps, alphabets]
    #  3. return max(steps)

    r, c = map(int, input().split())
    grid = tuple(tuple(str(char) for char in input().rstrip()) for _ in range(r))

    print(find_max_steps(grid))
