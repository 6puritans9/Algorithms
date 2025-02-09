import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_max_value(items, max_weight):
    dp = [0 for _ in range(max_weight + 1)]

    for item in items:
        weight = item[0]
        value = item[1]
        for sack_limit in range(max_weight, weight - 1, -1):
            dp[sack_limit] = max((value + dp[sack_limit - weight]), dp[sack_limit])

    return dp


if __name__ == "__main__":
    n, max_weight = list(map(int, get_input().split()))
    items = []
    for _ in range(n):
        items.append(list(map(int, get_input().split())))

    result = get_max_value(items, max_weight)
    print(result[max_weight])
