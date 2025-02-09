import sys


def get_input():
    return sys.stdin.readline().rstrip()


class Graph:
    def __init__(self, n):
        self.nodes = []
        self.visited = [[False for i in range(n)] for _ in range(n)]
        self.cluster = []

    def find_and_add_edges(self, matrix):
        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if col:
                    self.nodes.append((row_idx, col_idx))

    def get_neighbours(self, node):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        temp = []

        for direction in directions:
            x, y = node
            neighbour = (x + direction[0], y + direction[1])
            new_x, new_y = neighbour
            if new_x >= 0 and new_y >= 0 and neighbour in self.nodes:
                temp.append(neighbour)

        return temp

    def dfs(self, node, count=0, sub_cluster=None):
        if not sub_cluster:
            sub_cluster = []

        sub_cluster.append(node)
        count += 1
        self.visited[node[0]][node[1]] = True
        neighbours = self.get_neighbours(node)
        for neighbour in neighbours:
            if neighbour in self.nodes and not self.visited[neighbour[0]][neighbour[1]]:
                return self.dfs(neighbour, count, sub_cluster)

        return self.cluster.append({"count": count, "root": node})


if __name__ == "__main__":
    n = int(get_input())
    depts = []
    for i in range(n):
        sub_dept = [int(num) for num in get_input()]
        depts.append(sub_dept)

    graph = Graph(n)
    graph.find_and_add_edges(depts)
    for node in graph.nodes:
        graph.dfs(node)

    result = []
    print()
