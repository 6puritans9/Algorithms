import sys

input = sys.stdin.readline


def min_pal_partitions(_input: list[str]) -> int:
    # TC = O(N^2)
    # SC = O(N^2)

    n = len(_input)

    # determine palindrome and store it in the dp table
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        dp[i][i + 1] = (_input[i] == _input[i + 1])  # base case for substrings of length 2 (paradox precaution)
    for length in range(3, n + 1):  # from length 3 to n
        for start in range(n - length + 1):
            end = start + length - 1
            dp[start][end] = (_input[start] == _input[end]) and dp[start + 1][
                end - 1]  # expand palindrome from inner state

    # dp_len[end] = minimum number of palindromic partitions for _input[0:end+1]
    dp_len = [float("inf") for _ in range(n)]
    for end in range(n):
        if dp[0][end]:  # the whole substring _input[0:end] is a palindrome
            dp_len[end] = 1
        else:
            for start in range(end):
                # if _input[start+1:end+1] is a palindrome,
                # then _input[0:end+1] can be partitioned as [0...start] | [start+1...end]
                if dp[start + 1][end]:
                    dp_len[end] = min(dp_len[end], dp_len[start] + 1)

    return int(dp_len[-1])


if __name__ == "__main__":
    # 1. For a given string, find sets of palindrome.
    # 2. If palindrome exists, print the minimum number of possible sets.
    # 3. Example:
    #       _input = "ABACABA"
    # 4. There are 4 kinds of palindrome sets:
    #       {A, B, A, C, A, B, A}
    #       {A, BACAB, A}
    #       {ABA, C, ABA}
    #       {ABACABA}

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. len(_input) <= 2.5 * 10^3

    # Approach
    # 1. This one is a very tricky palindrome problem.
    # 2. The goal is to find the minimum number of palindrome sets that the input string could make.
    # 3. A naive nested loop solution will surely take more than O(N^2) time.
    # 4. To solve this problem in due time,
    #       a. store the palindrome check in dp table
    #       b. get the minimum length with O(1) access
    # 5. dp[i][j] = is string[i:j] a palindrome?
    # 6. dp_len[end] = minimum number of palindromic partitions for _input[0:end+1]
    # 7. For every possible end index:
    #       - If the whole substring _input[0:end+1] is a palindrome, set dp_len[end] = 1.
    #       - Otherwise, for each possible split point `start`, check if _input[start+1:end+1] is a palindrome.
    #         If so, combine it with the best result up to `start`: dp_len[end] = min(dp_len[end], dp_len[start] + 1)
    # 8. This ensures we reuse previously computed results, reducing the total time complexity to O(N^2).
    # 9. Final answer is stored in dp_len[n - 1], which represents the whole input string.

    _input = [char for char in input().rstrip()]
    print(min_pal_partitions(_input))
