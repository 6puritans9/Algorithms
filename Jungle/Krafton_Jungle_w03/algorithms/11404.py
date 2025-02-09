import sys
import math

print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def floyd(edges_list, vertices):
    graph = [[math.inf for vertex in range(vertices)] for _ in range(vertices)]
    for i in range(vertices):
        graph[i][i] = 0

    for u, v, w in edges_list:
        graph[u - 1][v - 1] = min(graph[u - 1][v - 1], w)

    for neighbour in range(vertices):
        for src in range(vertices):
            for dst in range(vertices):
                graph[src][dst] = min(
                    graph[src][dst], graph[src][neighbour] + graph[neighbour][dst]
                )

    return graph


if __name__ == "__main__":
    n = int(get_input())
    m = int(get_input())
    edges = []
    for _ in range(m):
        edges.append([int(num) for num in get_input().split()])

    results = floyd(edges, n)
    for row in results:
        for element in row:
            if element == math.inf:
                print(str(0) + " ")
            else:
                print(str(element) + " ")
        print("\n")
