import sys

input = sys.stdin.readline


# Total TC = O(N^2) + O(M) = O(10^6) + O(10^5) == O(10^6) < 1000ms
# Total SC = 2 * O(N^2) = 160MiB < 256MB

class Solution:
    def __init__(self, n: int, grid: list[tuple[int, ...]]):
        self.n = n
        self.prefix_sum = [[0 for _ in range(n)] for _ in range(n)]
        self.fill_prefix_sum(grid)

    def fill_prefix_sum(self, grid: list[tuple[int, ...]]) -> None:
        # TC = O(N^2) = O(1024^2) < O(10^6) <= 1000ms
        # SC = O(N^2) = 2^20 * 4bytes = 80MiB
        n = self.n

        self.prefix_sum[0][0] = grid[0][0]

        for x in range(1, n):
            self.prefix_sum[0][x] = self.prefix_sum[0][x - 1] + grid[0][x]
        for y in range(1, n):
            self.prefix_sum[y][0] = self.prefix_sum[y - 1][0] + grid[y][0]

        for y in range(1, n):
            for x in range(1, n):
                self.prefix_sum[y][x] = self.prefix_sum[y - 1][x] + self.prefix_sum[y][x - 1] - \
                                        self.prefix_sum[y - 1][x - 1] + grid[y][x]

    def __sum_of_range(self, x1, y1, x2, y2) -> int:
        # TC = O(1)

        result = self.prefix_sum[y2][x2]

        if y1 > 0:
            result -= self.prefix_sum[y1 - 1][x2]
        if x1 > 0:
            result -= self.prefix_sum[y2][x1 - 1]
        if y1 > 0 and x1 > 0:
            result += self.prefix_sum[y1 - 1][x1 - 1]

        return result

    def print_sum_of_range(self, x1, y1, x2, y2):
        print(self.__sum_of_range(x1, y1, x2, y2))


if __name__ == "__main__":
    # 1. For a given N*N grid
    # 2. print the sum of numbers
    # 3. which ranges from (x1, y1) to (x2, y2)
    # 4. x = row, y = col

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= N <= 2^10
    # 2. 1 <= M <= 10^5
    # 3. 1 <= number <= 10^3

    # Approach
    # 1. This one appears to be a divide and conquer problem
    # 2. However, due to the time limit and the amount of the input,
    #       O(N^2) or O(N) cannot be an answer. O(NM) = O(2^10 * 10^5) > 1000ms
    # 3. Solution with pre-caching strategy is required
    # 4. Create a 2d prefix sum array to solve this in O(1)
    # 5. Fill prefix sum:
    #       pf[0][x] = pf[0][x-1] + grid[0][x]
    #       pf[y][0] = pf[y-1][0] + grid[y][0]
    #       pf[y][x] = pf[y-1][x] + pf[y][x-1] - pf[y-1][x-1] + grid[y][x] // subtract one of the overlapping sum
    # 6. Get the specific sum:
    #       if y1 > 0: // only subtract the row sum
    #           _sum = pf[y2][x2] - (pf[y1-1][x2])
    #       if x1 > 0: // only subtract the col sum
    #           _sum = pf[y2][x2] - (pf[y2][x1-1]
    #       if y1 > 0: // subtract both and add the overlapping sub
    #           sum = pf[y2][x2] - (pf[y1-1][x2] + pf[y2][x1-1]) + pf[y1-1][x1-1]

    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(tuple(int(num) for num in input().split()))

    solution = Solution(n, grid)

    for _ in range(m):
        y1, x1, y2, x2 = map(int, input().split())  # 1-based
        solution.print_sum_of_range(x1 - 1, y1 - 1, x2 - 1, y2 - 1)
