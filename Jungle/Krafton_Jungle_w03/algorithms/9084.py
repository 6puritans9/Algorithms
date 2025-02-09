import sys


def get_input():
    return sys.stdin.readline().rstrip()


def count(coins, target):
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]


if __name__ == "__main__":
    T = int(get_input())
    conditions = []
    results = []
    for i in range(T):
        variety = int(get_input())
        coins = [int(num) for num in get_input().split()]
        target_cost = int(get_input())
        conditions.append(
            {"variety": variety, "coins": coins, "target_cost": target_cost}
        )

    for condition in conditions:
        results.append(count(condition["coins"], condition["target_cost"]))
    print("\n".join(str(result) for result in results))
