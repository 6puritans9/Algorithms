import sys

input = sys.stdin.readline


def find_min_cost(C: int, data: list[tuple[int, int]]) -> int:
    # TC = O(C^2)
    # SC = O(C)

    dp = [float("inf") for _ in range(C + 1)]
    dp[0] = 0

    for customer in range(1, C + 1):
        for cost, new_customer in data:
            if new_customer >= customer:
                dp[customer] = min(dp[customer], cost)
            else:
                dp[customer] = min(dp[customer], dp[customer - new_customer] + cost)

    return dp[C]


if __name__ == "__main__":
    # 1. There are N cities,
    #    cost for an ad campaign in each city,
    #    data for how many customers will come for that investment given.
    # 2. The goal is to increase new customers to C.
    # 3. Find the minimum cost to reach the goal.

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 0 < C <= 10^3
    # 2. 0 < N <= 20
    # 3. 0 < cost <= 10^2

    # Approach
    # 1. dp

    C, n = map(int, input().split())
    data = []
    for _ in range(n):
        cost, customer = map(int, input().split())
        data.append((cost, customer))

    print(find_min_cost(C, data))
