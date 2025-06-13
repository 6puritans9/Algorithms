import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(candy_list: tuple[int, ...], graph: dict[int, list[int]], visited: list[bool], start: int) -> tuple[int, int]:
    # TC = O(N+M)
    # SC = O(N)
    global N, M, K

    length = 0
    candy_amount = 0

    q = deque([start])
    while q:
        node = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        length += 1
        candy_amount += candy_list[node]

        for nbr in graph[node]:
            q.append(nbr)

    return length, candy_amount


def find_max_candies(candy_list: tuple[int, ...], graph: dict[int, list[int]]) -> int:
    # TC = O(N+M) + O(N*K) = O(10^4 + 10^5) + O(10^4 * 3*10^3) == O(10^5 + 3*10^7) = O(3*10^7) <= 1000ms
    # SC = O(N) + O(K)

    global N, M, K

    components = []  # [(friends, candies) for _ in range(n)]
    visited = [False for _ in range(N + 1)]
    for i in range(1, N + 1):
        if not visited[i]:
            friends, candy = bfs(candy_list, graph, visited, i)
            components.append((friends, candy))

    dp = [0 for _ in range(K)]
    for size, candies in components:  # O(N)
        if size > K:
            continue

        for j in range(K - 1, size - 1, -1):  # O(K)
            dp[j] = max(dp[j], dp[j - size] + candies)

    return dp[K - 1]


if __name__ == "__main__":
    # 1. There are N kids, M edges, K limit given.
    # 2. Kid A is going to take candies from other kids.
    # 3. If he takes candies from a kid, he has to take all the candies from all the kid's friends.
    # 4. He can do so only up to K kids,
    #       which means if the number of a kid's friends >= K: Kid A can take 0 candy.
    # 5. Find the maximum amount of candy that he can take from other kids.

    # Constraints
    # TIME 1000ms
    # SPACE 1024MB
    # 1. 1 <= N <= 3 * 10^4
    # 2. 0 <= M <= 10^5
    # 3. 1 <= K <= min{ N, 3000 }

    # 4. 1 <= a, b <= N
    # 5. a != b

    # Approach
    # 1. Pre-compute length = (edges + 1) and the sum of values in each graph. O(N + K) == O(10^5)
    # 2. Knapsack the pre-computed table. O(N) = O(10^4)

    # 3. components = []
    # 4. components.append(bfs(n, graph, candies))

    # 5. dp = [0 for _ in range(k)]
    # 7. return dp[k-1]

    # 8. how should I handle overlaps? >> knapsack with each component not individual
    # 9. how should I handle the starting node? >> include in each component

    N, M, K = map(int, input().split())
    candy_list = (0,) + tuple(int(num) for num in input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(find_max_candies(candy_list, graph))
