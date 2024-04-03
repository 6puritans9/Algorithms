# 1. set in_degrees
# 2. check if an element has in_degree == 0 in in_degrees
# 2-1. if so, enqueue the element
# 2-2. decrement all the neighbours' in_degree by 1
# 3. repeat the step #2 until !queue

import sys
from collections import defaultdict
from collections import deque


def get_input():
    return sys.stdin.readline().rstrip()


def topological_sort(graph, number):
    in_degrees = [0 for i in range(number)]
    in_degrees[0] = None

    for vertex in graph:
        neighbours = graph[vertex]
        for neighbour in neighbours:
            in_degrees[neighbour] += 1

    q = deque()
    visited = [False] * number
    result = []
    for i in range(1, len(in_degrees)):
        if not visited[i] and not in_degrees[i]:
            visited[i] = True
            q.append(i)

    while q:
        cur_v = q.popleft()
        result.append(cur_v)
        if graph[cur_v]:
            for nxt_v in graph[cur_v]:
                in_degrees[nxt_v] -= 1
                if not visited[nxt_v] and not in_degrees[nxt_v]:
                    visited[nxt_v] = True
                    q.appendleft(nxt_v)

    return result


if __name__ == "__main__":
    graph = defaultdict(list)
    students, m = [int(num) for num in get_input().split()]
    for _ in range(m):
        from_vertex, to_vertex = [int(num) for num in get_input().split()]
        graph[from_vertex].append(to_vertex)
    result = topological_sort(graph, students + 1)  # adjusting index from 1
    print(" ".join(map(str, result)))
