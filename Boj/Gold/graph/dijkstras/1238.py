import sys
import heapq

input = sys.stdin.readline


def dijkstra(n: int, graph: list[list[tuple[int]]], start: int) -> list[int | float]:
    # TC = O((E+V)logV) => O((M+N)logN)
    # SC = O(N)

    distances = [float("inf") for _ in range(n + 1)]
    distances[start] = 0

    pq = [(0, start)]  # dist, node

    while pq:
        dist, cur_node = heapq.heappop(pq)

        for w, nb in graph[cur_node]:
            new_dist = dist + w
            if new_dist < distances[nb]:
                distances[nb] = new_dist
                heapq.heappush(pq, (new_dist, nb))

    return distances


if __name__ == "__main__":
    # 1. N cows are going to visit point X.
    # 2. A total of M unidirectional edges connects each vertex.
    # 3. Road Ri requires Ti time to traverse.
    # 4. Each cow takes the shortest path each time.
    # 4. As the weight of each edge might differ,
    #       the cost to visit and return could vary.
    # 5. Find the longest amount of time a cow must spend to visit and return.

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 1 <= N <= 10^3
    # 2. 1 <= X <= N
    # 3. 1 <= M <= 10^5
    # 4. 1 <= Ti <= 10^2

    # Approach
    # 1. The main time-consuming part is to find the shortest path for each cow,
    #       that should be done twice to compute the sum of visit and return cost.
    # 2. The cow at X always spend 0 time.
    # 3. For calculating the shortest path, using Dijkstra's will take O(2 * (M + N)logN) == O(10^5) < 1000ms.
    # 4. Iterate both distances lists, find the max distance and print O(2N) == O(10^3).
    # 5. Getting distances from X is quite straightforward.
    # 6. On the other hand, from i to X has two approaches:
    #       Iterate naively from 1 to N or use a reversed graph.
    #       O(V * (E+V)logE) vs. O((E+V)logE)
    #       Which the latter is much effective.

    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]  # from x to i
    reversed_graph = [[] for _ in range(n + 1)]  # from i to x
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((t, b))
        reversed_graph[b].append((t, a))

    dist_from_x = dijkstra(n, graph, x)
    dist_to_x = dijkstra(n, reversed_graph, x)

    max_time = 0
    for i in range(1, n + 1):  # 1-based
        max_time = max(max_time, dist_from_x[i] + dist_to_x[i])

    print(max_time)
