def find_max_subseq_len(n, k, numbers) -> int:
    # dp[i][j] represents the maximum sum of a subsequence
    # when considering the first i numbers with j negative numbers being selected up to k
    dp = [[-float("inf") for _ in range(k + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        number = numbers[i]

        # I struggled with this one because I was too fixated on previous dp approaches.
        # They all ended up to dp[i][j] = max(dp[i][j], dp[i][j] + something),
        # which doesn't fit here.
        if number >= 0:
            for j in range(k + 1):
                dp[i][j] = max(dp[i - 1][j] + number, number)
        else:
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j - 1] + number, number)

    return int(max(max(row) for row in dp))


if __name__ == "__main__":
    n, k = map(int, input().split())
    numbers = [0, *(int(num) for num in input().split())]

    print(find_max_subseq_len(n, k, numbers))
