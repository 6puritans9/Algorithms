import sys
from collections import deque

input = sys.stdin.readline


def find_lcs_with_length(str1: list[str], str2: list[str]) -> tuple[int, str]:
    # TC = O(N^2) = O(10^6) < 2000ms
    # SC = O(N^2)

    len_str1 = len(str1)
    len_str2 = len(str2)
    dp = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_len = dp[len_str1][len_str2]
    lcs_str = deque()
    i, j = len_str1, len_str2
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_str.appendleft(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str = "".join(map(str, lcs_str))

    return lcs_len, lcs_str


if __name__ == "__main__":
    # 1. Two strings are given.
    # 2. Find the longest common subsequence.
    # 3. Print the length of LCS on the first line,
    #       print the lcs itself on the second line.

    # Constraints
    # TIME 2000ms(Python 3 exclusive)
    # SPACE 256MB
    # 1. 0 < length <= 10^3

    # Approach
    # 1. A DP problem.
    # 2. Create a two-dimensional dp array.
    # 3. Dp[i][j] represents the length of lcs for the first i chars of str1 and the first j chars of str2
    # 4. Begin with initializing all the dp[0][j] and dp[i][0] with zeroes.
    # 5. if str1[i-1] == str2[j-1]:
    #        dp[i][j] = dp[i-1][j-1] + 1
    # 6. else:
    #       dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    # 7. Getting the lcs string should be handled afterward.
    # 8. Since I've got the dp table, going backward through dp is feasible.
    # 9. if str1[i-1] == str2[j-1]:
    #       str.append(char)
    # 10. else:
    #       dp[i-1][j] > dp[i][j-1]: # str1 has longer lcs
    #           i -= 1
    #       else:
    #           j -= 1

    str1 = [char for char in input().strip()]
    str2 = [char for char in input().strip()]

    results = find_lcs_with_length(str1, str2)
    for result in results:
        print(result)
