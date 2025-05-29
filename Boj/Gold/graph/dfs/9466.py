import sys

input = sys.stdin.readline


class Team:
    def __init__(self):
        self.n = int(input())
        self.selections = (0,) + tuple(int(num) for num in input().split())
        self.free_students = 0

    def __dfs(self, n: int, selections: tuple[int, ...]) -> int:
        # TC = O(N)
        # SC = O(N)

        non_team_count = 0
        visited = [False for _ in range(n + 1)]
        in_team = [False for _ in range(n + 1)]

        for start in range(1, n + 1):  # 1-based
            if visited[start]:
                continue
            path = []  # Store the history
            curr = start

            while not visited[curr]:
                visited[curr] = True
                path.append(curr)
                curr = selections[curr]

            if curr in path:
                cycle_start = path.index(curr)
                for i in range(cycle_start, len(path)):
                    in_team[path[i]] = True

        for i in range(1, n + 1):
            if not in_team[i]:
                non_team_count += 1

        return non_team_count

    def find_free_students(self):
        self.free_students = self.__dfs(self.n, self.selections)

    def print(self):
        print(self.free_students)


if __name__ == "__main__":
    # 1. This is a cycle detection problem.
    # 2. For given N students,
    #       each student chooses another student to make a team together.
    # 3. There are two conditions that can make a valid team:
    #       a. one chooses himself.
    #       b. selections make a cycle.
    # 4. Find the number of students that does not belong to any team.

    # Constraints
    # TIME 3000ms
    # SPACE 256MB
    # 1. 2 <= N <= 10^5

    # Approach
    # 1. The most intuitive solution is iterative DFS. O(N^2)
    # 2. To reduce redundant traversal for better time complexity, visited check is required. O(N)

    t = int(input())
    for _ in range(t):
        team = Team()
        team.find_free_students()
        team.print()
