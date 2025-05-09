import sys

input = sys.stdin.readline


def pre_compute(n: int, seq: tuple[int, ...]) -> list[list[bool]]:
    # TC = O(N^2 + N) = O(N^2)
    # SC = O(N^2)

    dp = [[False for _ in range(n)] for _ in range(n)]

    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1

            if seq[start] == seq[end]:
                if length == 1 or length == 2:
                    dp[start][end] = True
                else:
                    dp[start][end] = dp[start + 1][end - 1]

    return dp


def is_palindrome(dp: list[list[bool]], s: int, e: int) -> bool:
    return dp[s][e]


if __name__ == "__main__":
    # 1. N-length natural number sequence is given.
    # 2. S, E is given for M times,
    #       which asks from index s-1 to e-1 in the given sequence,
    #       does the subsequnece make a palindrome.
    # 3. Print 1 if true else 0

    # Constraints
    # TIME 500ms
    # SPACE 256MB
    # 1. 1 <= N <= 2 * 10^3
    # 2. 1 <= S <= E <= N
    # 3. 1 <= M <= 10^6

    # Approach
    # 1. If I naively iterate the sequence each time,
    #       O(10^3 * 10^6) > 500ms in worst case scenario.
    # 2. So this problem asks to utilize dynamic programming.
    # 3. Precompute dp[s][e] which represents the palindrome validity.
    # 4. It takes O(2 * N^2) = O(10^6) < 500ms

    n = int(input())
    sequence = tuple(int(num) for num in input().split())
    dp = pre_compute(n, sequence)

    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        print(1 if is_palindrome(dp, s - 1, e - 1) else 0)
