import sys
from collections import defaultdict

input = sys.stdin.readline


def find(parent, x) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)


def find_max_dockings(g: int, planes: list[int]) -> int:
    # TC = O(P*a(G))
    # SC = O(G)

    parent = [i for i in range(g + 1)]
    count = 0

    for plane in planes:
        dock = find(parent, plane)
        if dock == 0:
            break

        union(parent, dock, dock - 1)
        count += 1

    return count


# Greedy
# def find_max_dockings(g: int, planes: list[int]) -> int:
#     # TC = O(G)
#     # SC = O(G)
#
#     dockings = [False for _ in range(g + 1)]
#     indices = defaultdict(int)
#     count = 0
#
#     for plane in planes:
#         if not indices[plane]:
#             indices[plane] = plane
#         idx = indices[plane]
#
#         while dockings[idx] and idx > 0:
#             idx -= 1
#         if idx == 0:
#             return count
#         dockings[idx] = True
#         indices[plane] = idx
#         count += 1
#
#     return count


if __name__ == "__main__":
    # 1. There are G gates in an airport.
    # 2. Each gate is in range(1, G+1).
    # 3. P airplanes will arrive in due order,
    #       and you should dock each one to a gate for good.
    # 4. Each plane has Gi value, which represents its port availability from 1 to Gi.
    # 5. This process ends when a new plane cannot dock anywhere.
    # 6. Find the maximum number of airplanes that can be docked.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= G <= 10^5
    # 2. 1 <= P <= 10^5
    # 3. 1 <= Gi <= G

    # Approach
    # 1. This one requires backtracking. O(N^2)
    # 2. But the time complexity should be reduced into O(N) or (NlogN).
    # 3. Since the arrival order is immutable,
    #       the docking should be done in backwards.
    # 4. This will take O(N).

    # 5. dockings = [False for _ in range(g+1)]
    # 6. indices = {}
    #    count = 0
    # 7. for each Gi,
    #       if not indices[Gi]:
    #           indices[Gi] = Gi
    #       idx = indices[Gi]
    # 8. while dockings[idx] and idx > 0:
    #       idx -= 1
    #    if idx == 0:
    #       return count
    #    dockings[idx] = True
    #    indices[Gi] = idx
    #    count += 1

    g = int(input())
    p = int(input())
    planes = []
    for _ in range(p):
        planes.append(int(input()))

    print(find_max_dockings(g, planes))
