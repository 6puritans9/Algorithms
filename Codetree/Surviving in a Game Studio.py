# The idea of using three-dimensional array for solution came quite naturally for this case.
# However, translating this idea into an actual implementation is always challenging,
# especially when managing state transitions

def find_max_days(n) -> int:
    global MOD
    dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n + 1)]

    # Begin with dp[i][B][T]
    # B for bad, which accumulates consecutive
    # T for terrible, accumulates globally.
    dp[1][0][0] = 1
    dp[1][1][0] = 1
    dp[1][0][1] = 1

    for i in range(2, n + 1):
        for b in range(3):
            for t in range(3):
                # Resetting b to 0 is really tricky part in this problem.
                dp[i][0][t] = (dp[i][0][t] + dp[i - 1][b][t]) % MOD
                if b < 2:
                    dp[i][b + 1][t] = (dp[i][b + 1][t] + dp[i - 1][b][t]) % MOD
                # Here too.
                if t < 2:
                    dp[i][0][t + 1] = (dp[i][0][t + 1] + dp[i - 1][b][t]) % MOD

    # Sum up all valid sequences of length n.
    result = 0
    for b in range(3):
        for t in range(3):
            result = (result + dp[n][b][t]) % MOD

    return result


if __name__ == "__main__":
    MOD = 10 ** 9 + 7

    n = int(input())
    print(find_max_days(n))
