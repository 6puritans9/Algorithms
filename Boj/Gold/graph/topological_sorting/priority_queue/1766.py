import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline


def find_order(n: int, graph: dict[int, list[int]], in_degree: list[int]) -> list[int]:
    # TC = O((N+M)logN)
    # SC = O(N)

    order = []

    # init
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        node = heapq.heappop(heap)
        order.append(node)

        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                heapq.heappush(heap, neighbour)

    return order


if __name__ == "__main__":
    # 1. For given N problems in range(1, N+1),
    # 2. Difficulty of the problem increases as the number goes up.
    # 3. The order of solving problems follows these:
    #       a. All the problems must be solved.
    #       b. If there were pre-requisites, they must be solved first despite the number.
    #       c. Easier problems must be solved first.
    # 4. For example, there are 4 problems:
    #       a. 4 connects to 2
    #       b. 3 connects to 1
    #    then the order should be 3 1 4 2.
    # 5. Print the right order.

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= N <= 3.2 * 10^4
    # 2. 1 <= M <= 10^5
    # 3. For any input (A, B), A has to be solved before B

    # Approach
    # 1. This is a topological sorting problem.
    # 2. Map the connections with in-degree from the input.
    # 3. Start from nodes which has 0 in-degree,
    #       proceed with BFS.
    # 5. After each enqueue, the current queue should be sorted in increasing order. O(NlogN)
    # 6. So it will take O(N^2logN) < 2000ms << not true
    # 7. Min-heap can reduce the time complexity into O((N+M)logN):
    #       Why do we write O((N + M) log N) instead of just max(N log N, M log N)?
    #       Because both parts contribute independently to the total runtime, and you have to account for both:
    #           N log N: The cost to push and pop all nodes exactly once.
    #           M log N: The cost incurred when edges cause nodes' in-degree to drop to zero, triggering pushes.
    #       Since these happen sequentially as part of the algorithm, the total time is the sum of both costs.

    n, m = map(int, input().split())
    graph = defaultdict(list)
    in_degree = [0 for _ in range(n + 1)]  # 1-based
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        in_degree[v] += 1

    result = find_order(n, graph, in_degree)
    print(" ".join(map(str, result)))

    # Too slow
    # def find_order(n: int, graph: dict[int, list[int]], in_degree: list[int]) -> list[int]:
    #     # TC = O(NlogN)
    #     # SC = O(N)
    #
    #     order = []
    #
    #     # init
    #     q = deque()
    #     for i in range(1, n + 1):
    #         if in_degree[i] == 0:
    #             q.append(i)
    #
    #     # bfs
    #     while q:
    #         node = q.popleft()
    #         order.append(node)
    #
    #         for neighbour in graph[node]:
    #             in_degree[neighbour] -= 1
    #             if in_degree[neighbour] == 0:
    #                 q.append(neighbour)
    #
    #         # sort queue
    #         sorted_q = deque(sorted(q))
    #         q = sorted_q
    #
    #     return order
