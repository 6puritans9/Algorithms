import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(graph: defaultdict[int, set[int]], node: int, parent: int, counts: list[int]):
    subtree_size = 1

    for child in graph[node]:
        if child != parent:
            subtree_size += dfs(graph, child, node, counts)

    counts[node] = subtree_size
    return subtree_size


def pre_compute(graph: defaultdict[int, set[int]], n: int, root: int) -> list[int]:
    # TC = O(N)
    # SC = O(N)

    counts = [0 for _ in range(n + 1)]  # 1-based
    dfs(graph, root, -1, counts)

    return counts


if __name__ == "__main__":
    # 1. A non-directional tree with root is given.
    # 2. All the given tree is guaranteed to be valid.
    # 3. With the number of vertices N, the number of root R, the number of queries Q,
    # 4. Find out the number of vertices that belong to vertex U.

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 2 <= N <= 10^5
    # 2. 1 <= R <= N
    # 3. 1 <= Q <= 10^5
    # 4. 1 <= U, V (U != V) <= N

    # Approach
    # 1. I can manage connections with dictionary.
    # 2. To avoid duplicate edge inputs, defaultdict(set) structure is feasible.
    # 3. Add the connection between u, v into dict[u], dict[v].
    # 4. For each query, if I traverse through any edge, it is not guaranteed that it traverses downward.
    # 5. So I can make a reference table from root which records the number of children nodes.
    # 6. Since it is O(N) task, O(10^5) can be solved in 1000ms.
    # 7. It will also take O(N) = 4byte * 10^5 = 400KB

    n, r, q = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    number_of_children = pre_compute(graph, n, r)

    for _ in range(q):
        u = int(input())
        print(number_of_children[u])
