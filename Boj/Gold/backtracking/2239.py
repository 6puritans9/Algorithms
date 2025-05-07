import sys

input = sys.stdin.readline


def backtrack(grid, rows, cols, boxes, empty_cells, idx):
    # TC = O(9^(N^2)) = O(9^81) in worst case scenario,
    # but it works in practice due to filled cells and pruning.

    if idx == len(empty_cells):
        return True

    i, j = empty_cells[idx]
    box_idx = (i // 3) * 3 + j // 3

    for num in range(1, 10):
        if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
            grid[i][j] = num
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_idx].add(num)

            if backtrack(idx + 1):
                return True

            # Backtrack
            grid[i][j] = 0
            rows[i].remove(num)
            cols[j].remove(num)
            boxes[box_idx].remove(num)

    return False


def play(grid):
    # SC = O(81) = O(1)

    # Pre-compute used numbers for faster lookup
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    empty_cells = []

    # Initialize sets and find empty cells
    for i in range(9):
        for j in range(9):
            num = grid[i][j]
            if num:
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)
            else:
                empty_cells.append((i, j))

    backtrack(grid, rows, cols, boxes, empty_cells, 0)


if __name__ == "__main__":
    grid = []
    for _ in range(9):
        grid.append(list(map(int, input().strip())))

    play(grid)

    for line in grid:
        print("".join(map(str, line)))

# Too Slow
# def in_row(grid, row, num):
#     return num in grid[row]
#
#
# def in_col(grid, col, num):
#     for row in range(0, 9):
#         if num == grid[row][col]:
#             return True
#
#     return False
#
#
# def in_sub_grid(grid, row, col, num):
#     box_row, box_col = 3 * (row // 3), 3 * (col // 3)
#
#     for r in range(box_row, box_row + 3):
#         for c in range(box_col, box_col + 3):
#             if grid[r][c] == num:
#                 return True
#     return False
#
#
# def is_valid(grid, row, col, num):
#     return not in_row(grid, row, num) and not in_col(grid, col, num) and not in_sub_grid(grid, row, col, num)
#
#
# def find_empty(grid):
#     for row in range(9):
#         for col in range(9):
#             if not grid[row][col]:
#                 return row, col
#     return None
#
#
# def backtrack(grid):
#     empty = find_empty(grid)
#     if not empty:
#         return True
#
#     row, col = empty
#
#     for num in range(1, 10):
#         if is_valid(grid, row, col, num):
#             grid[row][col] = num
#
#             if backtrack(grid):
#                 return True
#
#             # reset
#             grid[row][col] = 0
#
#     return False
#
#
# def play(grid: list[list[int]]) -> None:
#     backtrack(grid)


# if __name__ == "__main__":
# 1. A 9 * 9 sudoku table is given for T test cases.
# 2. The table is divided into nine 3 * 3 smaller squares.
# 3. Some cells contain decimal digits while others are empty.
# 4. Fill the empty spaces with digits from 1 to 9 to form a valid sudoku solution.

# Constraints
# TIME 2000ms
# SPACE 256MB
# 1. rows, cols = 9, 9

# Approach
# 1. This one seems to be a backtracking problem.
# 2. Empty cells are represented by 0 in the input table.
# 3. Each empty cell can be filled with a digit from 1 to 9,
# 4. but only if that digit is not already present in the same row, col, or 3*3 subgrid.
# 5. If no valid digit can be placed,
#       backtrack to the previous step.
# 6. The tricky part is checking subgrids.
# 7. 1) y < 3 and x < 3
#    2) y < 3 and 3 <= x < 6
#    3) y < 3 and 6 <= x < 9
#    4) 3 <= y < 6 and x < 3
#    5) 3 <= y < 6 and 3 <= x < 6
#    6) 3 <= y < 6 and 6 <= x < 9
#    7) 6 <= y < 9 and x < 3
#    8) 6 <= y < 9 and 3 <= x < 6
#    9) 6 <= y < 9 and 6 <= x < 9
# 8. Normalize the coordinate by dividing by 3 and multiply by 3 again.
# 9. Start by finding empty cell and fill it recursively in-place.
#
# LENGTH = 9
#
# sudoku = []
# for _ in range(LENGTH):
#     line = list(map(int, input().strip()))
#     sudoku.append(line)
#
# play(sudoku)
# for line in sudoku:
#     print("".join(map(str, line)))
