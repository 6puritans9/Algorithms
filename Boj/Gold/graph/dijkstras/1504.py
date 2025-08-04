import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def dijkstra(n: int, graph: dict[int, list[tuple[int, int]]], start: int):
    distances = [float("inf") for _ in range(n + 1)]
    distances[start] = 0

    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distances[node]:
            continue

        for neighbour, weight in graph[node]:
            if distances[neighbour] > cost + weight:
                distances[neighbour] = cost + weight
                heapq.heappush(heap, (distances[neighbour], neighbour))

    return distances


def find_min_dist(n: int, graph: dict[int, list[tuple[int, int]]], v1: int, v2: int) -> int:
    # TC = O((N+E) * logN)
    # SC = O(3N) = O(3 * N * 4bytes)

    dist_from_start = dijkstra(n, graph, 1)
    dist_from_v1 = dijkstra(n, graph, v1)
    dist_from_v2 = dijkstra(n, graph, v2)

    # 1 >> v1 >> v2 >> N
    path1 = dist_from_start[v1] + dist_from_v1[v2] + dist_from_v2[n]
    # 1 >> v2 >> v1 >> N
    path2 = dist_from_start[v2] + dist_from_v2[v1] + dist_from_v1[n]

    result = min(path1, path2)
    return result if result != float("inf") else -1


if __name__ == "__main__":
    # 1. A non-directional graph is given
    # 2. The goal is to find the shortest path to vertex N from vertex 1.
    # 3. A given pair of vertices(v1, v2) must be visited
    # 4. The visited vertices or edges can be traversed multiple times
    # 5. Find the shortest path which meets the requirements.
    #       if none, print -1

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 2 <= vertices <= 8 * 10^2
    # 2. 0 <= edges <= 2 * 10^5
    # 3. 1 <= dist < = 10^3
    # 4. v1 != v2, v1 != N, v2 != 1
    # 5. Only one edge can exist between two vertices(u, v)

    # Approach
    # 1. This is a bit trickier dijkstra problem.
    # 2. The weird point in this problem is that I can re-visit a vertex while all the weights are positive.
    #       a. Even with brute-force, there is no reason to go back and search from the previous node,
    #           because it only adds up.
    # 3. The only thing I should keep in mind is that v1, v2 must be visited.
    # 4. Set the initial value for each node infinite.
    # 5. Using heapq, update the shortest path
    # 6. There can be three paths:
    #       a. 1 >> v1 >> v2 >> N
    #       b. 1 >> v2 >> v1 >> N
    #       c. unreachable
    # 7. calculate each separately:
    #       a. 1 to N
    #       b. v1 to N
    #       c. v2 to N
    # 8. print the result

    n, e = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(e):
        u, v, dist = tuple(map(int, input().split()))
        graph[u].append((v, dist))
        graph[v].append((u, dist))
    v1, v2 = map(int, input().split())

    print(find_min_dist(n, graph, v1, v2))
