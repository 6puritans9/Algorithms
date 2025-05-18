import sys
from collections import defaultdict, deque

input = sys.stdin.readline


class Game:
    # TC = O(N + K) = O(10^3 + 10^5) = O(10^5)
    # SC = O(N)

    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.delays = (0,) + tuple(int(num) for num in input().split())  # 1-based

        self.graph = defaultdict(list)
        self.in_degree = [0 for _ in range(self.n + 1)]
        for _ in range(self.k):
            x, y = map(int, input().split())
            self.graph[x].append(y)
            self.in_degree[y] += 1

        self.w = int(input())

    def __bfs(self, n, w, graph: defaultdict, in_degree: list[int], delays: tuple[int, ...]) -> int:
        starts = []
        for i in range(1, n + 1):
            if not in_degree[i]:
                starts.append(i)

        q = deque(starts)
        dp = [0 for _ in range(n + 1)]
        for node in starts:
            dp[node] = delays[node]

        while q:
            node = q.popleft()
            # if node == w:
            #     break  # no pruning

            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                dp[neighbour] = max(dp[neighbour], dp[node] + delays[neighbour])

                if in_degree[neighbour] == 0:
                    q.append(neighbour)

        return dp[w]

    def play(self) -> int:
        return self.__bfs(self.n, self.w, self.graph, self.in_degree, self.delays)


if __name__ == "__main__":
    # 1. This is a building construction game.
    # 2. There are N buildings,
    #       and the order of construction K is given as X, Y,
    #       which means Y can start after finishing X.
    # 3. Every construction takes given delay Di.
    # 4. Multiple constructions can be done at the same time if possible.
    # 5. Find the minimum time to build W.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 1 <= N <= 10^3
    # 2. 1 <= K <= 10^5
    # 3. 1 <= x, Y, W <= N
    # 4. 0 <= Di <= 10^5
    # 5. Every construction is possible for all the test cases.

    # Approach
    # 1. This is a topological sorting problem.
    # 2. Make an adjacency list that represents the edges and directions among nodes.
    #       graph[x].append(y)
    # 3. If a connection is established, increment the in_degree of its destination.
    # 4. Find all the starting nodes which have zero in_degree,
    #       and enqueue them to apply BFS.
    # 5. Decrement the in_degree of neighbours for each visit.
    # 6. Record the delay in dp table, which was initialized to 0,
    #       dp[v] = max(dp[v], dp[u] + delays[v])
    # 7. return dp[W]

    t = int(input())
    for _ in range(t):
        game = Game()
        result = game.play()
        print(result)
