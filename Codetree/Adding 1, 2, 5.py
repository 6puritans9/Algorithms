# This one was pretty easy. Love it!

def get_subsets(n) -> int:
    conditions = (1, 2, 5)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for condition in conditions:
            if i >= condition:
                dp[i] += dp[i - condition]

    return dp[n] % 10007


if __name__ == "__main__":
    n = int(input())
    print(get_subsets(n))
