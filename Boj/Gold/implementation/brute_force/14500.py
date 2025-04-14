import sys

input = sys.stdin.readline

# Global variables
grid = []
visited = []


def in_range(y, x, rows, cols):
    return 0 <= y < rows and 0 <= x < cols


def dfs(y: int, x: int, rows: int, cols: int, depth: int, total: int) -> int:
    # TC = O(NM * 4^3) == O(NM)
    #   >> exploring 3 more cells from start,
    #   >> which has 4 choices for each level
    #   >> that concludes in O(4^3)
    # SC = O(1)

    global grid, visited

    if depth == 4:
        return total

    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    cur_sum = total  # Initialize with total for cases with no valid neighbors

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if in_range(ny, nx, rows, cols) and not visited[ny][nx]:
            visited[ny][nx] = True
            cur_sum = max(cur_sum, dfs(ny, nx, rows, cols, depth + 1, total + grid[ny][nx]))
            visited[ny][nx] = False

    return cur_sum


def check_t_shapes(y, x, rows, cols) -> int:
    # TC = O(1)
    # SC = O(1)

    global grid

    t_shapes = [
        [(0, -1), (0, 0), (0, 1), (1, 0)],
        [(0, -1), (0, 0), (1, 0), (-1, 0)],
        [(0, -1), (0, 0), (-1, 0), (0, 1)],
        [(-1, 0), (0, 0), (1, 0), (0, 1)]
    ]

    max_sum = 0

    for shape in t_shapes:
        cur_sum = 0

        for dy, dx in shape:
            ny, nx = y + dy, x + dx
            if in_range(ny, nx, rows, cols):
                cur_sum += grid[ny][nx]
            else:
                break
        else:
            max_sum = max(max_sum, cur_sum)

    return max_sum


def find_max_area_sum(rows: int, cols: int) -> int:
    # TC = O(NM)
    # SC = O(NM)

    global grid, visited

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    max_sum = 0

    for y in range(rows):
        for x in range(cols):
            visited[y][x] = True
            max_sum = max(max_sum, dfs(y, x, rows, cols, 1, grid[y][x]), check_t_shapes(y, x, rows, cols))
            visited[y][x] = False

    return max_sum


if __name__ == "__main__":
    # For given N*M sized grid,
    # By placing a tetromino of 5 distinct shapes,
    # maximize the value that it covers.
    # Tetorominoes can rotate.

    # Constraints
    # TIME 2000ms
    # SPACE 512MB
    # 1. 4 <= N, M <= 500
    # 2. 1 <= Grid element <= 10^3

    # Approach
    # 1. Grid area can be stretched up to 5^2 * 10^4
    #   computation for each cell can be up to 5 shapes * 4 rotation
    #   = O(25* 10^4 * 20) = O(5 * 10^6) <= 1000ms
    # 2. Implementing possible tetrominoes using bfs,
    #       because manual implementation can result in human error.
    # 3. Boundary check is required.

    n, m = map(int, input().split())  # rows, cols
    grid = []
    for _ in range(n):
        cols = [int(num) for num in input().split()]
        grid.append(cols)
    print(find_max_area_sum(n, m))
