import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_count(coins, coins_size, target_cost):
    usable_coins = coins
    result = []
    target = target_cost

    for i in range(coins_size):
        if coins[i] > target_cost:
            usable_coins = coins[:i]
            break

    for coin in reversed(usable_coins):
        quantity = target // coin
        result.append([coin, quantity])
        target -= coin * quantity

    return result


if __name__ == "__main__":
    N, K = [int(num) for num in get_input().split()]
    coins = []
    for i in range(N):
        coins.append(int(get_input()))

    results = get_count(coins, N, K)
    print(sum(result[1] for result in results))
