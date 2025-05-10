import sys

input = sys.stdin.readline


def find_min_cost(n: int, costs: list[tuple[int, ...]]) -> int:
    # TC = O(3^3 * N) = O(N)
    # SC = O(N)

    dp = [[[float("inf") for _ in range(3)] for _ in range(3)] for _ in range(n)]

    for colour in range(3):
        dp[0][colour][colour] = costs[0][colour]

    for i in range(1, n):
        for cur_colour in range(3):
            for first_colour in range(3):
                if i == n - 1 and cur_colour == first_colour:
                    continue

                for prv_colour in range(3):
                    if cur_colour != prv_colour:
                        dp[i][cur_colour][first_colour] = min(dp[i][cur_colour][first_colour],
                                                              dp[i - 1][prv_colour][first_colour] + costs[i][
                                                                  cur_colour])

    min_cost = float("inf")
    for j in range(3):
        for k in range(3):
            min_cost = min(min_cost, dp[n - 1][j][k])

    return min_cost


if __name__ == "__main__":
    # 1. N houses are on a one-dimensional line
    #       with 1-based number.
    # 2. Each house can be painted with red or green or blue.
    # 3. There are three specific constraints.
    #       a. house 1 should be different from house 2 and house N.
    #       b. house N should be different from house N-1 and house 1.
    #       c. house i(2 <= i <= N-1) should be different from house i-1 and house i+1.
    # 4. Each house has different cost to paint in each colour.
    # 5. Find the minimum cost of painting all the houses within the constraints.

    # Constraints
    # TIME 500ms
    # SPACE 128MB
    # 1. 2 <= N <= 10^3
    # 2. 1 <= cost <= 10^3

    # Approach
    # 1. A dp problem.
    # 2. One of the main constraint is that house[1] should be different from house[n].
    # 3. And also all the house[i-1], house[i], house[i+1] should choose different colours.
    # 4. Record the best costs for each step.
    # 5. dp[1] = [r, g, b]
    #    dp[2] = [min(g,b) + costs[1][0], min(r,b) + costs[1][1], min(r,g) + costs[1][2]]
    #    ...
    #    dp[n-1] = [min(dp[i-2][1], dp[i-2][2]) + costs[n-2]
    # 6. Actually, a three-dimensional array is required to solve this problem,
    #       because the initial selection matters to the last house.
    # 7. So dp[i][j][k] represents [i] for current house index, [j] for previous colour, [k] for first colour.

    n = int(input())
    costs = []
    for _ in range(n):
        r, g, b = map(int, input().split())
        costs.append((r, g, b))
    print(find_min_cost(n, costs))
