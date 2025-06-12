import sys

input = sys.stdin.readline


def ccw(pa: tuple[int, int], pb: tuple[int, int], pc: tuple[int, int]) -> int:
    x1, y1 = pa
    x2, y2 = pb
    x3, y3 = pc

    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


def is_collinear(pa, pb, pc, pd) -> bool:
    return ccw(pa, pb, pc) == 0 and ccw(pa, pb, pd) == 0


def does_overlap(pa, pb, pc, pd) -> bool:
    # TC = O(1)
    # SC = O(1)

    x1, y1 = pa
    x2, y2 = pb
    x3, y3 = pc
    x4, y4 = pd

    left1, right1 = min(x1, x2), max(x1, x2)
    left2, right2 = min(x3, x4), max(x3, x4)

    bottom1, top1 = min(y1, y2), max(y1, y2)
    bottom2, top2 = min(y3, y4), max(y3, y4)

    x_overlap = left1 <= right2 and left2 <= right1
    y_overlap = bottom1 <= top2 and bottom2 <= top1

    return x_overlap and y_overlap


def segments_intersect(pa: tuple[int, int], pb: tuple[int, int], pc: tuple[int, int], pd: tuple[int, int]) -> bool:
    # both segments intersect
    if ccw(pa, pb, pc) * ccw(pa, pb, pd) <= 0 and ccw(pc, pd, pa) * ccw(pc, pd, pb) <= 0:
        return True

    # both segments are parallel with overlaps
    if is_collinear(pa, pb, pc, pd) and does_overlap(pa, pb, pc, pd):
        return True

    return False


if __name__ == "__main__":
    # 1. Two lines, L1 and L2, are given on a 2D plane.
    # 2. L1 is defined by the points (x1, y1), (x2, y2).
    #    L2 by (x3, y3), (x4, y4).
    # 3. Print 1 if the two lines interset; otherwise, print 0.
    # 4. If a point on one line lies on another line, it is also considered an intersection.

    # Constraints
    # TIME 250ms
    # SPACE 512MB
    # 1. -10^6 <= xi, yi <= 10^6
    # 2. 0 < len(L1), len(L2)

    # Approach
    # 1. This is rather a geometry problem than an actual algorithm.
    # 2. CCW can determine if two lines were parallel or not.
    # 3. If they are parallel,
    #       they will intersect if both line segments share a point at least.
    # 4. Else if they are not,
    #       they will intersect if point C and point D are on the opposite side of line AB,
    #       also point A and point B are on the opposite side of line CD.

    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    pa = (x1, y1)
    pb = (x2, y2)
    pc = (x3, y3)
    pd = (x4, y4)

    result = segments_intersect(pa, pb, pc, pd)
    print(1 if result else 0)
