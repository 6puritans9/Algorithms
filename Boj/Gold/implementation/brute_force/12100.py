import sys

input = sys.stdin.readline
up, down, left, right = 0, 1, 2, 3


# TC = O(4^5 * N^2)
# SC = O(N^2)

def slide(line: list[int]) -> list[int]:
    return [x for x in line if x != 0]


def merge(line: list[int]) -> list[int]:
    merged = []
    skip = False

    for i in range(len(line)):
        if skip:
            skip = False
            continue

        if i + 1 < len(line) and line[i] == line[i + 1]:
            merged.append(line[i] * 2)
            skip = True
        else:
            merged.append(line[i])

    return merged


def move(n: int, board: list[list[int]], direction: int):
    # TC = O(N^2)
    # SC = O(N^2)

    new_board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if direction == up:
            line = [board[j][i] for j in range(n)]
            merged = merge(slide(line))
            for j in range(len(merged)):
                new_board[j][i] = merged[j]

        elif direction == down:
            line = [board[j][i] for j in range(n - 1, -1, -1)]
            merged = merge(slide(line))
            for j in range(len(merged)):
                new_board[n - 1 - j][i] = merged[j]

        elif direction == left:
            line = board[i]
            merged = merge(slide(line))
            for j in range(len(merged)):
                new_board[i][j] = merged[j]

        else:
            line = board[i][::-1]
            merged = merge(slide(line))
            for j in range(len(merged)):
                new_board[i][n - 1 - j] = merged[j]

    return new_board


def dfs(n: int, board: list[list[int]], depth: int) -> int:
    # TC = O(4^5)
    # SC = O(1)

    if depth == 5:
        return max(map(max, board))

    result = 0
    for d in range(4):
        next_board = move(n, board, d)
        if next_board != board:
            result = max(result, dfs(n, next_board, depth + 1))
        else:
            result = max(result, max(map(max, board)))

    return result


if __name__ == "__main__":
    # 1. An N*N grid is given.
    # 2. For each turn, a four-directional movement occurs.
    # 3. If two blocks having the same weight collided, they add up.
    # 4. An added block cannot be added again in the same turn.
    # 5. Find the maximum possible weight in 5 turns.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 1 <= N <= 20
    # 2. 2 <= block <= 2^10

    # Approach
    # 1. Every branch in the decision tree should be computed.
    # 2. To reduce the time complexity, apply memoization. O(5 * 4 * N^2)
    # 3. dp[index][last_direction][current_direction]
    # 4. up: iterate from row 0 to n-1
    #    down: iterate from row 0 to n-1
    #    left: iterate from col 0 to n-1
    #    right: iterate from col n-1 to 0
    # 5. If blocks added up, fill 0 in the corresponding cell.
    # 6. Return max block from dp[5][i][j]

    n = int(input())
    grid = []
    for _ in range(n):
        row = [int(num) for num in input().split()]
        grid.append(row)

    print(dfs(n, grid, 0))


# import sys
# from copy import deepcopy
#
# input = sys.stdin.readline
# up, down, left, right = 0, 1, 2, 3
#
#
# def in_range(y, x, n) -> bool:
#     return 0 <= y < n and 0 <= x < n
#
#
# def add(table, r, nr, c, nc) -> None:
#     table[r][c] *= 2
#     table[nr][nc] = 0
#
#
# def slide(n, table, direction) -> None:
#     if direction == up:
#         for r in range(n):
#             for c in range(n):
#                 nr = r + 1
#                 while not table[r][c] and in_range(nr, c, n):
#                     if not table[nr][c]:
#                         nr += 1
#                         continue
#                     table[r][c] = table[nr][c]
#                     table[nr][c] = 0
#
#     elif direction == down:
#         for r in range(n - 1, -1, -1):
#             for c in range(n):
#                 nr = r - 1
#                 while not table[r][c] and in_range(nr, c, n):
#                     if not table[nr][c]:
#                         nr -= 1
#                         continue
#                     table[r][c] = table[nr][c]
#                     table[nr][c] = 0
#
#     elif direction == left:
#         for r in range(n):
#             for c in range(n):
#                 nc = c + 1
#                 while not table[r][c] and in_range(r, nc, n):
#                     if not table[r][nc]:
#                         nc += 1
#                         continue
#                     table[r][c] = table[r][nc]
#                     table[r][nc] = 0
#
#     else:
#         for r in range(n):
#             for c in range(n-1, -1, -1):
#                 nc = c - 1
#                 while not table[r][c] and in_range(r, nc, n):
#                     if not table[r][nc]:
#                         nc -= 1
#                         continue
#                     table[r][c] = table[r][nc]
#                     table[r][nc] = 0
#
#
# def move_up(n: int, table: list[list[int]]) -> None:
#     for r in range(n):
#         for c in range(n):
#             cur_block = table[r][c]
#             is_added = False
#
#             for nr in range(r + 1, n):
#                 nxt_block = table[nr][c]
#                 if cur_block == nxt_block and not is_added:
#                     add(table, r, nr, c, c)
#                     is_added = True
#                 else:
#                     slide(n, table, up)
#
#
# def move_down(n: int, table: list[list[int]]) -> None:
#     for r in range(n - 1, -1, -1):
#         for c in range(n):
#             cur_block = table[r][c]
#             is_added = False
#
#             for nr in range(r - 1, -1, -1):
#                 nxt_block = table[nr][c]
#                 if cur_block == nxt_block and not is_added:
#                     add(table, r, nr, c, c)
#                     is_added = True
#                 else:
#                     slide(n, table, down)
#
#
# def move_left(n: int, table: list[list[int]]) -> None:
#     for r in range(n):
#         for c in range(n):
#             cur_block = table[r][c]
#             is_added = False
#
#             for nc in range(c + 1, n):
#                 nxt_block = table[r][nc]
#                 if cur_block == nxt_block and not is_added:
#                     add(table, r, r, c, nc)
#                     is_added = True
#                 else:
#                     slide(n, table, left)
#
#
# def move_right(n: int, table: list[list[int]]) -> None:
#     for r in range(n):
#         for c in range(n - 1, -1, -1):
#             cur_block = table[r][c]
#             is_added = False
#
#             for nc in range(c - 1, -1, -1):
#                 nxt_block = table[r][nc]
#                 if cur_block == nxt_block and not is_added:
#                     add(table, r, r, c, nc)
#                     is_added = True
#                 else:
#                     slide(n, table, right)
#
#
# def play(n, grid) -> int:
#     # TC = O(N^2)
#     # SC = O(N^2 * 4^2 * 6) = 16bytes * 16 * 6 = 2^8 * 6 == 6KB
#
#     dp = [[[[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)] for _ in range(4)] for _ in range(6)]
#     for i in range(4):
#         for j in range(4):
#             dp[0][i][j] = deepcopy(grid)
#
#     for i in range(1, 6):
#         for last_dir in range(4):
#             for cur_dir in range(4):
#                 table = dp[i][last_dir][cur_dir]
#                 if cur_dir == up:
#                     move_up(n, table)
#                 elif cur_dir == down:
#                     move_down(n, table)
#                 elif cur_dir == left:
#                     move_left(n, table)
#                 else:
#                     move_right(n, table)
#
#     max_block = 0
#     for i in range(n):
#         for j in range(n):
#             table = dp[5][i][j]
#
#             for r in range(n):
#                 for c in range(n):
#                     max_block = max(max_block, table[r][c])
#
#     return max_block
#
#
# if __name__ == "__main__":
#
#     n = int(input())
#     grid = []
#     for _ in range(n):
#         row = [int(num) for num in input().split()]
#         grid.append(row)
#
#     print(play(n, grid))
