import sys

input = sys.stdin.readline


# TC = O(NE)
# SC = O(N+E)

class TimeMachine:
    def __init__(self):
        n, m, w = map(int, input().split())
        self.nodes = n
        self.graph = self.init_graph(n)

        for _ in range(m):
            s, e, t = map(int, input().split())
            self.graph[s].append((t, e))
            self.graph[e].append((t, s))  # bidirectional paths
        for _ in range(w):
            s, e, t = map(int, input().split())
            self.graph[s].append((-t, e))  # unidirectional wormholes

    def init_graph(self, n: int):
        # SC = O(N+E)

        graph = [[] for _ in range(n + 1)]
        # Create dummy node to all other nodes with weight 0
        for i in range(n + 1):
            graph[0].append((0, i))

        return graph

    def traverse_and_find_result(self):
        # TC = O(NE)
        # SC = O(N)

        n = self.nodes
        dist = [float("inf") for _ in range(n + 1)]
        dist[0] = 0

        for _ in range(n):  # outer loop O(V)
            for u in range(n + 1):  # inner loop O(E)
                for time, nb in self.graph[u]:
                    if dist[u] != float("inf") and dist[u] + time < dist[nb]:
                        dist[nb] = dist[u] + time

        # Check negative cycle
        for u in range(n + 1):
            for time, nb in self.graph[u]:
                if dist[u] != float("inf") and dist[u] + time < dist[nb]:
                    return "YES"

        return "NO"

    def run(self):
        result = self.traverse_and_find_result()
        print(result)


if __name__ == "__main__":
    # 1. N farms are given.
    # 2. Each farm is connected with M paths.
    #       paths are bidirectional.
    # 3. There are W wormholes on the field.
    # 4. Wormholes are unidirectional
    #       and traversing through them rewinds T time.
    # 4. Starting from any node, traverse through wormholes,
    # 5. Find if one can get back to the starting point before the time he left.
    # 6. Print "YES" if one can, else "NO".

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= N <= 5 * 10^2
    # 2. 1 <= M <= 25 * 10^2
    # 3. 1 <= W <= 2 * 10^2
    # 4. 1 <= F <= 5
    # 5. -10^5 <= distance <= 10^5

    # Approach
    # 1. This is a bellman-ford problem handling negative weights.
    # 2. Iterating from 1 to 500,
    # 3. Find if the starting point can have a negative cycle.
    # 4. It will take O(VE) = O(N(M+W)) = O(500 * 2700) = O(5 * 2.7 * 10^5) < 2000ms.

    # This is a refined approach
    # 1. The goal is to detect a negative cycle in a directed graph.
    # 2. The graph may not guarantee that all nodes are connected to each other.
    #       Which means I need to account for the possibility of disconnected components,
    #       when checking for negative cycles.
    # 3. By introducing a dummy node that connects to all other nodes with zero-weight edges,
    #       instead of running Bellman-Ford for each node individually,
    #       it allows to check for negative cycles in just a single run.
    # 4. After Bellman-Ford iteration, a negative cycle check iteration has to be done.
    # 5. For each edge u->v,
    #       if dist[u] != float("inf"), which means unreachable,
    #       and dist[u] + weight < dist[v],
    #       it means there's still a way to relax this edge
    #       and that indicates a negative cycle.
    # 6. Return "Yes" | "NO" for the result.

    f = int(input())
    for _ in range(f):
        timeMachine = TimeMachine()
        timeMachine.run()
