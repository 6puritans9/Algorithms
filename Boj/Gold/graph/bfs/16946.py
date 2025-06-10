import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def in_range(y, x, rows, cols) -> bool:
    return 0 <= y < rows and 0 <= x < cols


def find(parent: list[list[tuple[int, int]]], r: int, c: int) -> tuple[int, int]:
    if parent[r][c] == (r, c):
        return parent[r][c]

    pr, pc = parent[r][c]
    parent[r][c] = find(parent, pr, pc)
    return parent[r][c]


def union(parent: list[list[tuple[int, int]]], size: list[list[int]], r1: int, c1: int, r2: int, c2: int) -> None:
    root1 = find(parent, r1, c1)
    root2 = find(parent, r2, c2)

    if root1 != root2:
        _r1, _c1 = root1
        _r2, _c2 = root2
        if size[_r1][_c1] > size[_r2][_c2]:
            parent[_r2][_c2] = root1  # attach root2 to root1
            size[_r1][_c1] += size[_r2][_c2]
        else:
            parent[_r1][_c1] = root2
            size[_r2][_c2] += size[_r1][_c1]


def find_possible_routes(rows: int, cols: int, grid: list[list[int]]) -> list[list[int]]:
    # TC = O(NM * a(NM)) == O(10^6) < 2000ms
    # SC = O(NM)

    result = [[0 for _ in range(cols)] for _ in range(rows)]
    parent = [[(r, c) for c in range(cols)] for r in range(rows)]
    size = [[1 for _ in range(cols)] for _ in range(rows)]

    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    # path compression
    for y in range(rows):
        for x in range(cols):
            if grid[y][x]:  # wall
                continue

            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx

                if in_range(ny, nx, rows, cols) and not grid[ny][nx]:
                    union(parent, size, y, x, ny, nx)

    # find
    for y in range(rows):
        for x in range(cols):
            if grid[y][x]:  # only for walls
                visited = set()
                count = 1
                for dy, dx in zip(dys, dxs):
                    ny, nx = y + dy, x + dx

                    if in_range(ny, nx, rows, cols) and not grid[ny][nx]:
                        root = find(parent, ny, nx)
                        if root not in visited:
                            visited.add(root)
                            pr, pc = root
                            count += size[pr][pc]

                result[y][x] = count % 10

    return result


if __name__ == "__main__":
    # 1. An N*M sized map is given.
    # 2. Each tile can have either one of the following states:
    #       0 for reachable,
    #       1 for unreachable.
    # 3. One can proceed to neighbouring 4 directions from a reachable tile.
    # 4. For each tile in the map,
    #       if the tile is 1, assume that it was 0.
    #       after that, find the reachable number of tiles.
    # 5. Print the result for each tile in the given map:
    #       if the tile is a wall, print modulo 10.
    #       else if the tile was 0, print 0.

    # Constraints
    # TIME 2000ms
    # SPACE 512MB
    # 1. 1 <= N <= 10^3
    # 2. 1 <= M <= 10^3

    # Approach
    # 1. This will take up to O((NM)^2) naively.
    # 2. Because O(NM) search is unavoidable, which will take up to O(10^6) < 1000ms,
    #       the inner loop inside the outer loop should be reduced to something close to O(N).
    # 3. This can be achieved with disjoint set, O(NM * a(NM)) == O(NM) < 2000ms.
    # 4. There are two things that make this problem complicated:
    #       a. as the grid is two-dimensional, find() should handle rows and cols.
    #       b. because the wall can toggle, mark it as a parent of its neighbours might be problematic.

    # 5. Handling case a:
    #       initialize parent[r][c] = (r,c)
    # 6. Handling case b:
    #       while iterate each cell in grid:
    #          if grid[y][x] == 0:
    #            for (ny, nx) in 4 directions which is not grid[ny][nx] == 1:
    #               union(y, x, ny, nx)
    # 7. To calculate reachable cells in the result and compute union operation efficiently,
    #       manage the state with 'size' array.
    # 8. Attach the small set to the bigger one.
    # 9. Store sum of all the sizes by modulo 10.
    #       if not grid[y][x]: result[y][x] = 0
    # 10. Return

    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = [int(num) for num in input().rstrip()]
        grid.append(row)

    result_grid = find_possible_routes(n, m, grid)
    for row in result_grid:
        print("".join(map(str, row)))
