import sys
from collections import deque

input = sys.stdin.readline


def in_range(x):
    global BOUNDARY

    return 0 <= x <= BOUNDARY


def find_min_time(x: int, target: int) -> int:
    # TC = O(N) = O(10^5) < 1000ms
    # SC = O(1) + O(N) = 100,001bytes + 2 * 4bytes * 10^5 == 100KB + 800KB = 900KB

    global BOUNDARY

    visited = [False for _ in range(BOUNDARY + 1)]
    queue = deque([(x, 0)])

    while queue:
        cx, count = queue.popleft()
        if cx == target:
            return count

        if visited[cx]:
            continue
        visited[cx] = True

        # Jump
        if in_range(cx * 2) and not visited[cx * 2]:
            queue.append((cx * 2, count))

        # Walk
        for dx in [-1, 1]:
            nx = cx + dx

            if in_range(nx) and not visited[nx]:
                queue.append((nx, count + 1))

    return 0


# Incorrect
# def find_min_time(x: int, y: int) -> int:
#     if y < x:
#         return x - y
#     if y == x:
#         return 0
#
#     while y >= 2 * x:
#         x *= 2
#
#     temp_x = x
#     count = 0
#     while 2 * temp_x > y:
#         temp_x -= 1
#         count += 1
#         if x - temp_x > y - x:
#             return y - x
#
#     return count


if __name__ == "__main__":
    # 1. (x, y) are on point (n, k)
    # 2. x can move to +1, -1 or 2*x
    # 3. 2*x move takes 0 sec while the others take 1 sec
    # 4. Find the minimum amount of time that x takes to find y

    # Constraints
    # TIME 2000ms
    # SPACE 512MB
    # 1. 0 <= N <= 10^5
    # 2. 0 <= K <= 10^5

    # Approach
    # 1. if y == x: return 0
    # 2. x can only jump to positive direction
    #       which means if y < x: return x-y
    # 3. Because it takes no time to jump to 2*x,
    #       in greedy approach, jumps have to be made
    # 4. if y >= 2*x: jump
    #    else:
    #       temp_ x = x
    #       if y-temp_x >= y-x: return y-x
    #       if y < 2*temp_x:
    #          temp_x -= 1
    # => Greedy approach skips optimal solution like case 6 18

    # 0-1 BFS
    # 1.

    BOUNDARY = 100000
    n, k = map(int, input().split())
    print(find_min_time(n, k))
