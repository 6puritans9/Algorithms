import sys

input = sys.stdin.readline


def transform(a: list[list[int]], b: list[list[int]], n: int) -> list[list[int]]:
    multiplied = [[0 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            for k in range(n):
                multiplied[r][c] = (multiplied[r][c] + a[r][k] * b[k][c]) % 1000

    return multiplied


def cut_in_half(matrix: list[list[int]], n: int, b: int) -> list[list[int]]:
    # TC = O(logB)
    # SC = O(N^2)

    if b == 0:
        return IDENTITY
    if b == 1:
        return [[matrix[r][c] % 1000 for c in range(n)] for r in range(n)]

    if b % 2 == 0:
        half = cut_in_half(matrix, n, b // 2)
        return transform(half, half, n)
    else:
        return transform(matrix, cut_in_half(matrix, n, b - 1), n)


if __name__ == "__main__":
    # 1. An N*N sized matrix A is given.
    # 2. Compute A**B.
    # 3. To prevent overflow, store (el % 10^3) for each el.
    # 4. Print the result as the form of given matrix.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 2 <= N <= 5
    # 2. 1 <= B <= 10^11
    # 3. 0 <= element <= 10^3

    # Approach
    # 1. This problem asks to find the result of transformation A after B times.
    # 2. A naive iteration is impossible to get in 1000ms.
    # 3. A special technique, Matrix exponentation by squaring, is the key.
    # 4. A*A = A^2
    #    A^2 * A^2 = A^4
    #    A^4 * A^4 = A^8
    # 5. This will make the time complexity down to O(logN) == 11*log10 < 1000ms.

    # The geometric meaning of this problem
    # If A represents a rotation by 30°, then:
    #   A^2 rotates by 60°
    #   A^12 rotates by 360° (full circle, back to original)
    #   A^B rotates by (30° × B)

    N, B = map(int, input().split())
    matrix = [[int(num) for num in input().split()] for _ in range(N)]

    IDENTITY = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        IDENTITY[i][i] = 1

    result = cut_in_half(matrix, N, B)
    for row in result:
        print(" ".join(map(str, row)))
