import sys


def get_input():
    return sys.stdin.readline().rstrip()


class Graph:
    def __init__(self, height, width):
        self.matrix = [[] for i in range(height)]
        self.visited = [[False for i in range(width)] for _ in range(height)]
        self.count = 0

    def set_matrix(self, row):
        self.matrix[i] = [letter for letter in row]

    def check_width(self):
        for r_idx, row in enumerate(self.matrix):
            for c_idx, col in enumerate(row):
                if not self.visited[r_idx][c_idx]:
                    self.visited[r_idx][c_idx] = True
                    if col == "-":
                        self.count += 1
                        neighbour = [r_idx, c_idx + 1]
                        while neighbour[1] < width:
                            x, y = neighbour
                            if self.matrix[x][y] == "-":
                                self.visited[x][y] = True
                            else:
                                break
                            neighbour[1] += 1

                    else:
                        self.check_height(r_idx, c_idx)

    def check_height(self, row, col):
        for r_idx, row in enumerate(self.matrix):
            for c_idx, col in enumerate(row):
                if not self.visited[r_idx][c_idx]:
                    self.visited[r_idx][c_idx] = True
                    if col == "|":
                        self.count += 1
                        neighbour = [r_idx + 1, c_idx]
                        while neighbour[0] < height:
                            x, y = neighbour
                            if self.matrix[x][y] == "|":
                                self.visited[x][y] = True
                            else:
                                break
                            neighbour[0] += 1


if __name__ == "__main__":
    height, width = map(int, get_input().split())
    graph = Graph(height, width)

    for i in range(height):
        graph.set_matrix(get_input())

    graph.check_width()

    print(graph.count)
