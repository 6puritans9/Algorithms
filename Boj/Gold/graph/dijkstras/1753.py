import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


def find_shortest_path(V: int, start: int, edges: list[tuple[int, int, int]]) -> list[int | float]:
    # TC = O(ElogV) == O(10^5 * log10^4) < 1000ms
    # SC = O(V + E) = O(4bytes*2*10^4 + 8bytes*3*10^5) = 80KB + 2400KB

    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))

    distances = [float("inf") for _ in range(V)]
    distances[start] = 0

    hq = [(0, start)]
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distances[node]:
            continue

        for weight, neighbour in graph[node]:
            new_dist = dist + weight

            if new_dist < distances[neighbour]:
                distances[neighbour] = new_dist
                heapq.heappush(hq, (new_dist, neighbour))

    return distances


if __name__ == "__main__":
    # 1. A directed graph is given.
    # 2. Every weight of each edge is natural number n <= 10.
    # 3. From starting node K,
    # 4. Find the shortest path to V.
    # 5. Print path to starting point as 0,
    #       and print "INF" if there's no edge to the next vertex.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= V <= 2 * 10^4
    # 2. 1 <= E <= 3 * 10^5
    # 3. 1 <= K <= V
    # 4. 1 <= w <= 10

    # Approach
    # 1. Iterate all the edges to push connections into a defaultdict(list). O(E)
    # 2. Create a heapq.
    # 3. Use Dijkstra to find the shortest path. O(ElogV)
    # 4. Return and print each distance in the shortest path list.

    V, E = map(int, input().split())
    K = int(input())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))

    distances = find_shortest_path(V, K - 1, edges)
    for distance in distances:
        print(distance if distance != float("inf") else "INF")
