import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_dp(num):
    dp = [0] * (num + 1)
    dp[0] = 1
    if num > 0:
        dp[1] = 1
    if num > 1:
        dp[2] = 2
    if num > 2:
        dp[3] = 4

    for i in range(4, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp


if __name__ == "__main__":
    T = int(get_input())
    numbers = []

    for i in range(T):
        numbers.append(int(get_input()))

    table = get_dp(max(numbers))
    for number in numbers:
        print(table[number])
