import sys
from itertools import combinations

input = sys.stdin.readline


def find_house(n, grid):
    # TC = O(N^2)
    # SC = O(N^2)

    houses = []
    stores = []

    for y in range(n):
        for x in range(n):
            if grid[y][x] == 1:
                houses.append((y, x))
            elif grid[y][x] == 2:
                stores.append((y, x))

    return houses, stores


def find_min_dist(m: int, houses: list[tuple[int, int]],
                  stores: list[tuple[int, int]]) -> int:
    # TC = O(comb(len(stores), m) * len(houses) * m)
    # SC = O(1)

    result = float("inf")

    for comb in combinations(stores, m):
        cur_dist = 0

        for house in houses:
            hy, hx = house
            min_dist = float("inf")
            for sy, sx in comb:
                dist = abs(hy - sy) + abs(hx - sx)
                min_dist = min(min_dist, dist)
            cur_dist += min_dist

        result = min(result, cur_dist)

    return result


if __name__ == "__main__":
    # 1. An N*N sized city is given.
    # 2. Each cell is 0, empty | 1, house | 2, store.
    # 3. The distance between two points is abs(r1 - r2) + abs(c1 - c2).
    # 4. To minimize the cost, only M stores should be maintained.
    # 5. Find the minimized sum of distance, between stores and houses.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 2 <= N <= 50
    # 2. 1 <= M <= 13

    # Approach
    # 1. Pre-compute possible distances from a house to each store.
    # 2. By removing stores, find the minimum distance.

    n, m = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    houses, stores = find_house(n, grid)

    print(find_min_dist(m, houses, stores))
