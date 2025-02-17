# A simple variant of the previous Subsequence Sum Equals M problem.
# I think I'm getting accustomed to this kind of problem.

def find_equal_max_sum(numbers, n) -> bool:
    total_sum = sum(numbers)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        cur_num = numbers[i]

        for part_sum in range(total_sum + 1):
            if part_sum >= cur_num and dp[i - 1][total_sum - part_sum]:
                dp[i][part_sum] = True
            elif dp[i - 1][part_sum - cur_num]:
                dp[i][part_sum] = True

    for i in range(n + 1):
        for j in range(total_sum + 1):
            if dp[i][j] and abs(total_sum - j) == j:
                return True

    return False


if __name__ == "__main__":
    n = int(input())
    numbers = [0, *[int(num) for num in input().split()]]

    print("Yes" if find_equal_max_sum(numbers, n) else "No")
