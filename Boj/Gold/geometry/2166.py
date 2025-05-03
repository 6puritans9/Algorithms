import sys

input = sys.stdin.readline


def get_area(n: int, coords: list[tuple[int, int]]) -> float:
    # TC = O(N)
    # SC = O(1)

    sum1 = 0
    sum2 = 0

    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]

        sum1 += x1 * y2
        sum2 += y1 * x2

    area = 0.5 * abs(sum1 - sum2)

    return area


if __name__ == "__main__":
    # 1. N dots are given on a two-dimensional plane.
    # 2. Calculate the area of the polygon.
    # 3. Print the area in the format of (round(num), 1)

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 3 <= N <= 10^4
    # 2. -10^5 <= x, y <= 10^5

    # Approach
    # 1. The area of a polygon can be deducted by shoelace formula.
    # 2. ((x1*y2 + x2*y3 + ... + xn*y1) - (y1*x2 + y2*x3 + ... + yn*x1)) * 0.5
    # 3. This will take O(N) time.

    n = int(input())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))

    result = get_area(n, coords)
    print(f"{result:.1f}")
