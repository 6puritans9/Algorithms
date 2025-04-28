import sys

input = sys.stdin.readline


def get_max_sum(n: int, triangle: list[list[int]]) -> int:
    # TC = O(N^2) = O(500^2) = O(25 * 10^4) < 2000ms
    # SC = O(1)

    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]


if __name__ == "__main__":
    # 1. A triangle of numbers is given.
    # 2. Each row contains the n numbers.
    # 3. From the root of the triangle,
    #       one of the binary path is possible to proceed.
    # 4. Find the maximum sum of the numbers in selected path.

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= n <= 5 * 10^2

    # Approach
    # 1. A dp-like approach is feasible.
    # 2. Climb up from the bottom of the triangle.
    # 3. for i in range(n-2, -1, -1):
    #       for j in range(len(triangle[i]):
    #           triangle[i][j] = max(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
    # 4. return triangle[0][0]

    n = int(input())
    triangle = []
    for _ in range(n):
        numbers = [int(num) for num in input().split()]
        triangle.append(numbers)

    print(get_max_sum(n, triangle))
