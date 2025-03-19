import sys

input = sys.stdin.readline


def backtrack(n: int, row: int, cols: list[bool], diags1: list[bool], diags2: list[bool]) -> int:
    # TC = O(N!)
    # SC = O(1)

    if row == n:
        return 1

    count = 0

    for col in range(n):
        if cols[col]:
            continue
        if diags1[row + col]:
            continue
        if diags2[row - col + (n - 1)]:
            continue

        cols[col] = True
        diags1[row + col] = True
        diags2[row - col + (n - 1)] = True

        count += backtrack(n, row + 1, cols, diags1, diags2)

        cols[col] = False
        diags1[row + col] = False
        diags2[row - col + (n - 1)] = False

    return count


def find_solution(n: int) -> int:
    # parameters: n, row, cols, diag1, diag2

    cols = [False for _ in range(n)]
    diags1 = [False for _ in range(n * 2 - 1)]  # bottom-right
    diags2 = [False for _ in range(n * 2 - 1)]  # bottom-left

    return backtrack(n, 0, cols, diags1, diags2)


if __name__ == "__main__":
    # For an N*N sized board,
    # find the number of valid ways to place N queens

    # 1 <= N <= 15
    # Time limit = 10000ms, Memory limit = 128MB
    # Brute-force approach of O(N^N) is infeasible

    # 1. Start placing queens from row 0
    # 2. Due to the rules of chess, each row can have only one queen
    # 3. Maintain a set of occupied columns to prevent column conflicts
    # 4. Use two sets to track diagonal conflicts:
    #       - diag1 = row + col(↘ top-left to bottom-right)
    #       - diag2 = row - col(↙ top-right to bottom-left)
    # 5. If a position is valid, place the queen and proceed to next row
    # 6. If all rows are filled, return 1
    # 7. Backtrack by removing the last placed queen and trying the next column

    n = int(input())

    print(find_solution(n))
