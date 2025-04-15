import sys

input = sys.stdin.readline


def find_min_cost(n: int, edges: tuple[int, ...], prices: tuple[int, ...]) -> int:
    # TC = O(N + len(edges)) = O(2N) = O(N)
    # SC = O(1)

    total_cost = 0
    i, j = 0, 1

    while j < n:
        if prices[j] >= prices[i] and j < n:
            j += 1
            continue

        for k in range(i, j):
            total_cost += (edges[k] * prices[i])
        i = j
        j += 1

    if not j < n and i < n:
        for k in range(i, j - 1):
            total_cost += (edges[k] * prices[i])

    return total_cost


if __name__ == "__main__":
    # 1. For given n number of cities,
    # each city is connected one by one
    # thorough an edge with weight.
    # 2. Each city has fuel price.
    # 3. The size of gas tank has no limit.
    # 4. Find the minimum cost to reach from left to the right end.

    # Constraints
    # Time
    # Space
    # 1. 2 <= N <= 10^5
    # 2. 1 <= total distance <= 10^9
    # 3. 1 <= price <= 10^9

    # Approach
    # 1. Naive iteration is not feasible due to time limit.
    # 2. Greedy approach with two pointer seems to work
    #       if price[i] >= price[j]:
    #           fill(dist(i-j))
    #       else:
    #           while price[j] >= price[i] and j < n:
    #               j += 1

    n = int(input())
    edges = tuple(int(num) for num in input().split())
    prices = tuple(int(num) for num in input().split())

    print(find_min_cost(n, edges, prices))
