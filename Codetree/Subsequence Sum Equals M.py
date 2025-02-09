def get_min_subset(m, seq) -> int:
    dp = [float("inf")] * (m + 1)
    dp[0] = 0

    for number in seq:
        # Descend all the way down to number - 1,
        # since dp[number] sets the starting point from 0
        for i in range(m, number - 1, -1):
            dp[i] = min(dp[i], dp[i - number] + 1)

    return dp[m] if dp[m] != float("inf") else -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    seq = [int(num) for num in input().split()]
    print(get_min_subset(m, seq))