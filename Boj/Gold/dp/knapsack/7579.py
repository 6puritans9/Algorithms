import sys

input = sys.stdin.readline


def best_replacement_cost(n: int, target: int, processes: tuple[int, ...], costs: tuple[int, ...]) -> int:
    # TC = O(N * sum(costs))
    # SC = O(sum(costs))

    sum_of_costs = sum(costs)
    dp = [0 for _ in range(sum_of_costs + 1)]

    for i in range(n):
        for j in range(sum_of_costs, costs[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - costs[i]] + processes[i])

    for i in range(sum_of_costs + 1):
        if dp[i] >= target:
            return i

    return 0


# Two-pointer approach
# def best_replacement_cost(n: int, target: int, processes: tuple[int, ...], costs: tuple[int, ...]) -> int:
#     # TC
#     # SC = O(N)
#
#     mapped = defaultdict(list)
#     for i in range(n):
#         mapped[processes[i]].append(costs[i])
#     sorted_map = sorted(mapped.keys())
#
#     min_cost = float("inf")
#     cur_cost = 0
#     left, right = 0, 0
#     while left < n:
#
#         if cur_cost >= target:
#             min_cost = min(min_cost, sum(sorted_map[left:right + 1]))
#             cur_cost -= sorted_map[left]
#             left += 1
#
#         while cur_cost < target and right < n-1:
#             right += 1
#             cur_cost += sorted_map[right]
#
#     return min_cost


if __name__ == "__main__":
    # 1. This is a process scheduling problem.
    # 2. For given N processes,
    #       each App Ai occupies Mi memory space.
    # 3. Ci represents the cost of resuming an app after it has been slept.
    # 4. To launch a new app B, memory M is required,
    #       which means some of A1, A2, ..., An needs to be slept.
    # 5. Find the minimum sum of costs that can free M bytes.

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 1 <= N <= 10^2
    # 2. 1 <= M <= 10^7
    # 3. 1 <= Mi <= 10^7
    # 4. 0 <= Ci <= 10^2
    # 5. M <= m1 + m2 + ... + mn

    # Approach
    # 1. This is either a two-pointer problem or a dp problem.
    # 2. Because each process has its own unique cost, sorting it would increase the complexity.
    # 3. Let's begin with two-pointer method.
    # 4. left, right = 0, 0
    # 5. while left < n:
    #       cur_sum = 0
    #       if cur_sum >= m:
    #           cur_sum -= costs[left]
    #           min_cost = min(min_cost, sum(costs[left:right+1])
    #           left += 1
    #           continue
    #       while cur_sum < m and right < n:
    #           right += 1
    #           cur_sum += costs[right]
    # 6. The thing is, if I used two-pointer method, it is not possible to get the optimal subset.
    # 7. So the remaining feasible option is dp.
    # 8. dp[i] = cost
    #       dp = [0 for range(sum_of_costs + 1)]
    # 9 . for i in range(n):
    #       for j in range(sum_of_costs, costs[i]-1, -1):
    #           dp[j] = max(dp[j], dp[j - costs[i]] + processes[i])

    n, m = map(int, input().split())
    on_memory = tuple(int(num) for num in input().split())
    costs = tuple(int(num) for num in input().split())

    print(best_replacement_cost(n, m, on_memory, costs))
