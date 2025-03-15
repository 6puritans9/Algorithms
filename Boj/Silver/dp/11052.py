import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_result(n, prices):
    dp = [0] * (n + 1)
    dp[1] = prices[0]

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(prices[i - 1], dp[i - j] + dp[j], dp[i])

    return dp[n]


if __name__ == "__main__":
    N = int(get_input())
    prices = [int(num) for num in get_input().split()]

    print(get_result(N, prices))
