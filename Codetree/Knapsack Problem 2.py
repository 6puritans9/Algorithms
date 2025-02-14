def get_max_value(jewels, m) -> int:
    dp = [0] * (m + 1)

    for w, v in jewels:
        if w > m:
            break
        for i in range(w, m + 1):
            dp[i] = max(dp[i], dp[i - w] + v)

    return max(dp)


if __name__ == "__main__":
    n, m = map(int, input().split())
    jewels = [tuple(int(num) for num in input().split()) for _ in range(n)]
    jewels.sort(key=lambda x: x[0])

    print(get_max_value(jewels, m))
