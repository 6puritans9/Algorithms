# This problem requires a whole new different perspective.
# At first, I began to approach with dp[i][j], j for +, - which acts as a prefix for each number,
# but soon I realized the tree which given numbers make cannot be contained into the two-dimensional array.

def find_choices(n, m, numbers) -> int:
    global LIMIT

    # Handling negative numbers in an array by shifting indices using an offset,
    # which is a really fancy approach indeed.
    offset = LIMIT

    # dp[i][s] stores the number of ways to reach sum 's' using the first 'i' numbers.
    # So dp should accumulate the number of ways to reach m, not the signs.
    dp = [[0 for _ in range(LIMIT * 2 + 1)] for _ in range(n)]
    dp[0][offset + numbers[0]] += 1
    dp[0][offset - numbers[0]] += 1

    for i in range(1, n):
        for s in range(-LIMIT, LIMIT + 1):
            if not dp[i - 1][offset + s]:
                continue

            number = numbers[i]
            # Ensuring the new sum stays within valid bounds before updating dp.
            if -LIMIT <= s + number <= LIMIT:
                dp[i][offset + s + number] += dp[i - 1][offset + s]
            if -LIMIT <= s - number <= LIMIT:
                dp[i][offset + s - number] += dp[i - 1][offset + s]

    # Remember to use 'offset + m' to properly index into the dp.
    return dp[n - 1][offset + m]


if __name__ == "__main__":
    LIMIT = 20

    n, m = map(int, input().split())
    numbers = [int(num) for num in input().split()]

    print(find_choices(n, m, numbers))
