import sys

input = sys.stdin.readline


def find(parent: list[int], x: int) -> int:
    # Find
    root = x
    while parent[root] != root:
        root = parent[root]

    # Compress
    while parent[x] != root:
        ancestor = parent[x]
        parent[x] = root
        x = ancestor

    return root


def union(parent: list[int], u: int, v: int) -> None:
    parent[find(parent, v)] = find(parent, u)


def detect_first_cycle_turn(edges: list[tuple[int, int]], n: int) -> int:
    parent = [i for i in range(n)]

    for i, (u, v) in enumerate(edges, start=1):
        if find(parent, u) == find(parent, v):
            return i
        union(parent, u, v)

    return 0


if __name__ == "__main__":
    # 1. This is a game called Cycle game.
    # 2. Two players draw a line between node u, v for each turn.
    # 3. At the start of the game, N points are given in the plane.
    # 4. And each of the points has a unique number range from (0, n),
    #       which no three points lie on the same line.
    # 6. Players take turns until there is the loser who completes a cycle first.
    # 7. Print the turn of forming the first cycle.
    # 8. If the game didn't finish until M, print 0.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 3 <= N <= 5 * 10^5
    # 2. 3 <= M <= 10^6

    # Approach
    # 1. The most common cycle detection implementation is using bfs,
    #       which takes O(V+E) time.
    # 2. 10^6 iteration for O(V+E) is too inefficient for the time limit.
    # 3. Another method is union-find.
    # 4. It determines if there's a cycle for de facto constant time. O(M) * O(1)

    # 5. Union-Find begins from every node having a parent of itself.
    # 6. For each (u, v) set in edges, set parent[v] = u
    #       which is recursive:
    #           parent[v] = parent[u] if parent[u] != u
    # 7. Store the information as parent[v] = find(parent[u]) for O(1) access.
    # 8. If find(u) == find(v), a cycle is detected:
    #       return Turn
    # 9. If it didn't reach an early return:
    #       return 0

    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    print(detect_first_cycle_turn(edges, n))
