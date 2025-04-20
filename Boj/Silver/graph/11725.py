import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def find_parent_node(n: int, edges: list[tuple[int, int]]) -> list[int]:
    # TC = O(N + N) = O(N)
    # SC = O(N)

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    parent = [0 for _ in range(n + 1)]
    queue = deque([1])
    vstd = [False for _ in range(n + 1)]

    while queue:
        cur_node = queue.popleft()
        if vstd[cur_node]:
            continue
        vstd[cur_node] = True

        for neighbour in graph[cur_node]:
            if not vstd[neighbour]:
                parent[neighbour] = cur_node
                queue.append(neighbour)

    return parent[2:]


if __name__ == "__main__":
    # 1. A tree without a root is given.
    # 2. Assuming that the root of this tree as 1,
    # 3. Print the parent nodes from node 2.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 2 <= N <= 10^5

    # Approach
    # 1. The root of the given tree is 1.
    # 2. If a node is connected to node 1, it's parent is 1.
    # 3. Create a graph using defaultdict which describes the connections.
    # 4. Start from root, traverse all the nodes and set the parent.
    # 5. Print the result from node 2

    # Example
    # 1 - 6 - 3 - 5
    # 1 - 4 - 2
    # 4 - 7

    n = int(input())
    edges = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edges.append((a, b))

    parents = find_parent_node(n, edges)
    for parent in parents:
        print(parent)
