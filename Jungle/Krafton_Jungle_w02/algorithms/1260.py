import collections
import sys


def get_input():
    return sys.stdin.readline().rstrip()


def dfs(matrix, size, start, visited=None):
    if visited is None:
        visited = [False] * size

    visited[start] = True
    print(start + 1, end=" ")
    for j in range(size):
        if matrix[start][j] == 1 and not visited[j]:
            dfs(matrix, size, j, visited)


def bfs(matrix, size, start):
    visited = [False] * size
    q = collections.deque([start])

    while q:
        node = q.popleft()
        if not visited[node]:
            visited[node] = True
            print(node + 1, end=" ")

            for j in range(size):
                if matrix[node][j] == 1 and not visited[j]:
                    q.append(j)


if __name__ == "__main__":
    n, m, v = [int(number) for number in get_input().split()]
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        i, j = [int(number) for number in get_input().split()]
        matrix[i - 1][j - 1] = 1
        matrix[j - 1][i - 1] = 1
    dfs(matrix, n, v - 1)
    print()
    bfs(matrix, n, v - 1)
