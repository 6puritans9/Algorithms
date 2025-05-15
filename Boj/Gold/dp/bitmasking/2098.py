import sys

input = sys.stdin.readline
INF = float("inf")


def min_cost(n: int, w: list[tuple[int, ...]]) -> int:
    # TC = O(2^N * N^2) = O(2^10 * 10^2) < 1000ms
    # SC = O(N * 2^N) == O(4bytes * 2^10) = 1kib

    # dp[mask][last] = minimum cost to visit all cities in mask and end at city 'last'
    dp = [[INF for _ in range(n)] for _ in range(1 << n)]
    dp[1][0] = 0
    result = INF

    for mask in range(1, 1 << n):  # 2*n loop
        for last in range(n):  # n loop
            if not (mask & (1 << last)):  # skip if 'last' is not visited in the current mask
                continue

            prv_mask = mask & ~(1 << last)
            if not prv_mask and last != 0:
                continue

            for prv in range(n):  # n loop
                if not ((prv_mask & (1 << prv)) and w[prv][last]):
                    continue

                dp[mask][last] = min(dp[mask][last], dp[prv_mask][prv] + w[prv][last])

    for last in range(1, n):
        if w[last][0]:
            result = min(result, dp[(1 << n) - 1][last] + w[last][0])

    return result


if __name__ == "__main__":
    # 1. A traveling salesman problem.
    # 2. Cities range from 1 to N are given,
    # 3. And each city might have edges or not.
    # 4. A salesman depart from a city and visit all the other cities,
    #       until he comes back to the origin city.
    # 5. Find the minimum cost for the traveling.

    # 6. Cost for travel is given as W[i][j],
    #       which represents cost from city i to city j.
    # 7. The cost for each one-way trip may vary.
    # 8. If it is not possible to reach city j, W[i][j] = 0

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 2 <= N <= 16
    # 2. 0 <= cost <= 10^6
    # 3. Every given case is valid.

    # Approach
    # 1. Use DP with bitmasking to track visited the current city.
    # 2. Let dp[mask][last] represent the minimum cost to visit all cities.
    # 3. Initialize dp[1][0] = 0, meaning we start at city 0 with only it visited.
    # 4. For each possible visited state 'mask' and for each city 'last' included in that mask:
    #     a. Compute 'prv_mask' by removing 'last' from 'mask'.
    #     b. For every possible previous city 'prv' in 'prv_mask':
    #         If a path exists from 'prv' to 'last', update dp[mask][last] using:
    #         dp[mask][last] = min(dp[mask][last], dp[prv_mask][prv] + w[prv][last])
    # 5. Finally, check all paths that visited every city and return to city 0,
    #    and pick the minimum cost among them.

    n = int(input())
    w = [tuple(int(num) for num in input().split()) for _ in range(n)]

    print(min_cost(n, w))
