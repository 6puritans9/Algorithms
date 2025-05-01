import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_node: int, n: int, graph: list[list]) -> tuple[int, int]:
    # TC = O(N + E)
    # SC = O(N)

    distances = [-1 for _ in range(n + 1)]
    distances[start_node] = 0

    farthest_node = start_node
    max_dist = 0

    q = deque([start_node])

    while q:
        cur_node = q.popleft()

        for nb, w in graph[cur_node]:
            if distances[nb] == -1:
                distances[nb] = distances[cur_node] + w
                q.append(nb)

                if distances[nb] > max_dist:
                    max_dist = distances[nb]
                    farthest_node = nb

    return farthest_node, max_dist


def find_diameter(n: int, graph: list[list]) -> int:
    # TC = O(2 * (N+E)) == O(N) < 2000ms

    farthest_node, _ = bfs(1, n, graph)
    _, diameter = bfs(farthest_node, n, graph)

    return diameter


if __name__ == "__main__":
    # 1. A tree with weighted edges is given.
    # 2. Suppose select 2 nodes and stretch all the edges between them.
    # 3. Its diameter will be the longest sum of the weights.
    # 4. Find the diameter.
    # 5. Input format: parent, (child, weight) until -1

    # Constraints
    # TIME 2000ms
    # SPACE 256MB
    # 1. 2 <= V <= 10^5
    # 2. 1 <= weight <= 10^4

    # Approach
    # 1. Create a list of adjacency
    # 2. Find the farthest node from root node
    # 3. Find the farthest node from previous farthest node

    v = int(input())
    adj_list = [[] for _ in range(v + 1)]
    for _ in range(v):
        _input = [int(num) for num in input().split()]
        parent = _input[0]

        neighbour = -1
        weight = -1
        for i in range(1, len(_input)):
            if _input[i] == -1:
                break
            # node
            if i % 2:
                neighbour = _input[i]
            # weight
            else:
                weight = _input[i]
                adj_list[parent].append((neighbour, weight))

    print(find_diameter(v, adj_list))
