import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_node, n: int, graph: list[list]) -> tuple[int, int]:
    # TC = O(N+E)
    # SC = O(N)
    distances = [-1 for _ in range(n + 1)]
    distances[start_node] = 0

    max_dist = 0
    farthest_node = start_node

    q = deque([start_node])

    while q:
        cur_node = q.popleft()

        for nb, w in graph[cur_node]:
            if distances[nb] == -1:  # also checks visited
                distances[nb] = distances[cur_node] + w
                q.append(nb)

                if distances[nb] > max_dist:
                    max_dist = distances[nb]
                    farthest_node = nb

    return farthest_node, max_dist


def find_diameter(graph: list[list], n: int) -> int:
    # TC = O(N+E) == O(N + (N-1)) = O(N) < 2000ms

    farthest_node, _ = bfs(1, n, graph)
    _, diameter = bfs(farthest_node, n, graph)

    return diameter


if __name__ == "__main__":
    # 1. A tree with weighted edges is given.
    # 2. Suppose select 2 nodes and stretch all the edges between them.
    # 3. Its diameter will be the longest sum of the weights.
    # 4. Find the diameter.
    # 5. Input format: parent, child, weight

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= n <= 10^4
    # 2. 1 <= weight <= 10^2

    # Approach
    # DP but too complex:
    # 1. Start from leaf nodes, if it has a sibling, add the weights and compare with current diameter.
    # 2. As this is a recursive pattern, use dp.
    # 3. Every tree starts from root node 1, and its children is 2, 3
    # 4. Store all the connections and make recursion with dp.

    # BFS:
    # 1. From the root node, find the farthest node.
    # 2. Start from that farthest node, find another farthest node.
    # 3. This will determine the diameter

    n = int(input())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        adj_list[parent].append((child, weight))
        adj_list[child].append((parent, weight))

    print(find_diameter(adj_list, n))
