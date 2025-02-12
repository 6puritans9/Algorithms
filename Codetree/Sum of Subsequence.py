# My first approach was storing the sum of subsequences in two-dimensional dp,
# and make a backward iteration to find the sum that equals m
# which makes the time complexity O(N^3)
# But it was not the optimal solution, obviously.

# So this one is the correct O(NM) solution,
# But this one is actually a bit slower than typical N * M iterations,
# because it has to copy the previous state for each iteration.

def find_sub_seq(n, seq, m) -> bool:
    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1].copy()
        for s in dp[i - 1]:
            new_sum = s + seq[i - 1]

            if new_sum == m:
                return True
            dp[i].add(new_sum)

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))

    result = find_sub_seq(n, seq, m)
    print("Yes" if result else "No")
