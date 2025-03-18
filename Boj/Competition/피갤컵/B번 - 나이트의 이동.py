def count_reachable_positions(n, r, c):
    # Adjust to 0-based indexing
    r -= 1
    c -= 1

    # Determine the parity of the starting position
    start_parity = (r + c) % 2

    if n % 2 == 0:
        return (n * n) // 2
    else:
        if start_parity == 0:
            return (n * n + 1) // 2
        else:
            return (n * n - 1) // 2


if __name__ == "__main__":
    n = int(input())
    r, c = map(int, input().split())
    print(count_reachable_positions(n, r, c))

# The snippet below is bfs solution O(N^2), which cannot meet the time limit

# from collections import deque
#
#
# def in_range(y, x, n):
#     return 0 <= y < n and 0 <= x < n
#
#
# def find_trails(n, start_y, start_x) -> int:
#     dys = [-2, -2, -1, -1, 1, 1, 2, 2]
#     dxs = [-1, 1, -2, 2, -2, 2, -1, 1]
#
#     queue = deque([(0, start_y, start_x)])  # (move_count, y, x)
#     possible_trails = set()
#     possible_trails.add((start_y, start_x))
#     visited = [[False for _ in range(n)] for _ in range(n)]
#
#     while queue:
#         mov, cy, cx = queue.popleft()
#         if visited[cy][cx]:
#             continue
#         visited[cy][cx] = True
#
#         if mov != 0 and not mov % 2:
#             possible_trails.add((cy, cx))
#
#         for dy, dx in zip(dys, dxs):
#             ny, nx = cy + dy, cx + dx
#
#             if in_range(ny, nx, n) and not visited[ny][nx]:
#                 queue.append((mov + 1, ny, nx))
#
#     return len(possible_trails)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     r, c = map(int, input().split())
#
#     print(find_trails(n, r - 1, c - 1))
