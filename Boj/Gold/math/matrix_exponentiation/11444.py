import sys

input = sys.stdin.readline


def multiply(mat1, mat2) -> list[list[int]]:
    global MOD

    # SC = O(1)

    result = [[0, 0], [0, 0]]

    result[0][0] = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % MOD
    result[0][1] = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % MOD
    result[1][0] = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % MOD
    result[1][1] = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % MOD

    return result


def matrix_power(base_matrix: list[list[int]], n) -> list[list[int]]:
    # TC = O(logN)
    # SC = O(logN)

    if n <= 1:
        return base_matrix

    # even
    if not n % 2:
        half_pow = matrix_power(base_matrix, n // 2)  # find base matrix by applying logarithmic property
        return multiply(half_pow, half_pow)

    # odd
    else:
        return multiply(base_matrix, matrix_power(base_matrix, n - 1))  # M_n * M_n-1


def nth_fibonacci(n: int) -> int:
    if n < 2:
        return n

    base_matrix = [[1, 1], [1, 0]]
    result = matrix_power(base_matrix, n - 1)

    return result[0][0]


if __name__ == "__main__":
    # 1. A natural number N is given.
    # 2. Find fibonacci number Fn.
    # 3. F0 = 0
    #    F1 = 1
    #    F2 = F0 + F1
    # 4. Print Fn % (10^9 + 7)

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 0 < N <= 10^18

    # Approach
    # 1. Typical DP O(N) cannot solve this problem
    # 2. From the time constraint, O(logN) approach is needed.
    #   => Matrix Exponentiation as ME
    # 3. ME recurs in this flow: [F(n+1), F(n)]ᵀ = [[1,1],[1,0]] × [F(n), F(n-1)]ᵀ
    # 4. Which is same as [F(n+1), F(n)]ᵀ = [[1,1],[1,0]]ⁿ × [F(1), F(0)]ᵀ = [[1,1],[1,0]]ⁿ × [1,0]ᵀ
    # 5. Instead of computing the matrix power naively in O(n) time, we use the divide-and-conquer approach:
    #       If n is even: M^n = (M^(n/2))²
    #       If n is odd: M^n = M × M^(n-1)
    # 6. nth_fibonacci sets up the base matrix and returns the result
    # 7. The multiply function handles matrix multiplication

    MOD = 10 ** 9 + 7

    n = int(input())
    print(nth_fibonacci(n))
