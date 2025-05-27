import sys
from collections import defaultdict, deque

input = sys.stdin.readline


class Schedule:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.graph = defaultdict(list)
        self.in_degree = [0 for _ in range(n + 1)]
        self.singers = []
        self.__prepare()

    def __prepare(self):
        for _ in range(self.m):
            _input = [int(num) for num in input().split()]
            len_input = _input[0]

            for i in range(1, len_input):
                u, v = _input[i], _input[i + 1]

                self.graph[u].append(v)
                self.in_degree[v] += 1

    def __bfs(self, n, graph, in_degree):
        # TC = O(V+E)
        # SC = O(N)

        q = deque()
        singers = []

        for i in range(1, n + 1):
            if not in_degree[i]:
                q.append(i)

        while q:
            node = q.popleft()
            singers.append(node)

            for neighbour in graph[node]:
                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    q.append(neighbour)

        # Exception Handling
        if len(singers) != n:
            return []

        return singers

    def plan(self):
        self.singers = self.__bfs(self.n, self.graph, self.in_degree)

    def print(self):
        if not len(self.singers):
            print(0)
            return

        for singer in self.singers:
            print(singer)


if __name__ == "__main__":
    # 1. This is a scheduling problem.
    # 2. There are N singers and M producers.
    # 3. Each producer can manage a singer queue,
    #       which can be overlapped among different producers.
    # 4. For example,
    #       a. 1 4 3
    #       b. 6 2 5 4
    #       c. 2 3
    #       the answer could be 621543 or 162543
    # 5. Find any valid order if there's one,
    #       if not, print 0.

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 1 <= N <= 10^3
    # 2. 1 <= M <= 10^2

    # Approach
    # 1. This is about processing the common elements with topological sorting.
    #       or a simple topological sorting problem since it accepts different answers.
    # 2. Assign a defaultdict(list) graph,
    #       and a list in_degree = [i for i in range(1, n+1)]
    # 3. As each given queue represents a linear sequence,
    #       for i in range(len(queue)-1):
    #           u, v = queue[i], queue[i+1]
    #           graph[u].append(v)
    #           in_degree[v] += 1
    # 4. Once step 3 is done, find the starting nodes by iterating in_degree which has 0 value.
    # 5. Using BFS, enqueue next node if in_degree == 0
    # 6. If it is no possible to traverse all the vertices, return 0.

    n, m = map(int, input().split())

    schedule = Schedule(n, m)
    schedule.plan()
    schedule.print()
