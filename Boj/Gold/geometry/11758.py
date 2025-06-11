import sys

input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3) -> int:
    direction = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if direction > 0:  # left turn
        return 1
    if direction < 0:  # right turn
        return -1
    return 0  # collinear


if __name__ == "__main__":
    # 1. Three dots, P1, P2, P3 are given on a 2D plane.
    # 2. Find out the direction of a line which connects P1, P2, P3 in due order.
    # 3. Print 1 if counter-clockwise,
    #       -1 if clockwise,
    #       0 if collinear.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. -10^4 <= xi, yi <= 10^4
    # 2. P1, P2, P3 has distinct coordinates.

    # Approach
    # 1. This is a ccw problem.
    # 2. Ccw determines the direction of two distinct vectors from the area they consist.
    # 3. vector B[(x2,y2),(x3,y3)] extends from vector A[(x1,y1),(x2,y2)]
    # 4. If they are collinear, they will make no parallelogram, which will result in 0.
    # 5. If B turns left, the signed area will be positive, and negative in the other case.

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    print(ccw(x1, y1, x2, y2, x3, y3))
