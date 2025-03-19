class Solution:
    def backtrack(self, n: int, row: int, results: list[list[str]], cols: list[bool], diag1: list[bool],
                  diag2: list[bool], cur_result) -> None:
        if row == n:
            results.append([*cur_result])
            return

        for col in range(n):
            if cols[col]:
                continue
            if diag1[row + col]:
                continue
            if diag2[row - col + (n - 1)]:
                continue

            cols[col] = True
            diag1[row + col] = True
            diag2[row - col + (n - 1)] = True

            row_str = "." * col + "Q" + "." * ((n - 1) - col)
            cur_result.append(row_str)
            self.backtrack(n, row + 1, results, cols, diag1, diag2, cur_result)
            cur_result.pop()

            cols[col] = False
            diag1[row + col] = False
            diag2[row - col + (n - 1)] = False

    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = [False for _ in range(n)]
        diag1 = [False for _ in range(n * 2 - 1)]
        diag2 = [False for _ in range(n * 2 - 1)]
        results = []

        self.backtrack(n, 0, results, cols, diag1, diag2, [])

        return results


if __name__ == "main__":
    n = int(input())
    solution = Solution(n)
