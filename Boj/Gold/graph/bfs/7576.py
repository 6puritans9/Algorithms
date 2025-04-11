import sys
from collections import deque

input = sys.stdin.readline


class TomatoRipener:
    def __init__(self, cols, rows, grid):
        self.cols = cols
        self.rows = rows
        self.grid = grid
        self.tomatoes_count = 0
        self.ripe_tomatoes = []
        self.analyze_grid()

    def analyze_grid(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] != -1:
                    self.tomatoes_count += 1
                if self.grid[r][c] == 1:
                    self.ripe_tomatoes.append((r, c))

    def are_all_tomatoes_ripe(self) -> bool:
        return len(self.ripe_tomatoes) == self.tomatoes_count

    def in_range(self, y, x) -> bool:
        return 0 <= y < self.rows and 0 <= x < self.cols

    def calculate_min_days(self) -> int:
        # TC = O(MN)
        # SC = O(MN)

        if self.are_all_tomatoes_ripe():
            return 0

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        queue = deque(self.ripe_tomatoes)
        visited = [[False for _ in range(m)] for _ in range(n)]
        days = 0
        ripe_count = len(self.ripe_tomatoes)

        while queue:
            # Process all tomatoes at the current day level
            cur_day_size = len(queue)

            for _ in range(cur_day_size):
                cy, cx = queue.popleft()
                if visited[cy][cx]:
                    continue
                visited[cy][cx] = True

                for dy, dx in zip(dys, dxs):
                    ny, nx = cy + dy, cx + dx

                    if (self.in_range(ny, nx) and
                            self.grid[ny][nx] == 0 and
                            not visited[ny][nx]):
                        self.grid[ny][nx] = 1
                        queue.append((ny, nx))
                        ripe_count += 1

            # Only increment date if there are more tomatoes to ripen
            if queue:
                days += 1

        return days if ripe_count == self.tomatoes_count else -1


if __name__ == "__main__":
    # A grid of states is given.
    # each state represents,
    #   -1 for null
    #   0 for non-ripe
    #   1 for ripe
    # ripe ones affect up, down, left, right to be ripe
    # Find the minimum date,
    # that all the tomatoes will be ripe
    # If all the tomatoes are already ripe, return 0
    # If not all tomatoes can be ripe, return -1

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 2 <= M, N <= 10^3

    # Approach
    # 1. Naive bfs will take O(MN) = O(10^3 * 10^3) = O(10^6) <= 1000ms

    m, n = map(int, input().split())  # cols, rows
    grid = []
    for _ in range(n):
        row = [int(num) for num in input().split()]
        grid.append(row)

    ripener = TomatoRipener(m, n, grid)

    print(ripener.calculate_min_days())
