import sys
from collections import deque, defaultdict

input = sys.stdin.readline


class Stage:
    # TC = O(HW)
    # SC = O(HW)

    def __init__(self):
        h, w = map(int, input().split())
        self.H, self.W = h, w
        self.GRID = [list(input().rstrip()) for _ in range(h)]

        keys = input().rstrip()
        self.KEYS = set(keys) if keys != '0' else set()
        self.RESULT = 0

    def __in_range(self, r, c):
        return 0 <= r < self.H and 0 <= c < self.W

    def try_add(self, visited, q, doors, r, c):
        if not self.__in_range(r, c) or visited[r][c]:
            return

        tile = self.GRID[r][c]
        if tile == '*':
            return

        visited[r][c] = True
        if tile == '$':
            self.RESULT += 1
            self.GRID[r][c] = '.'
        elif tile.islower():
            if tile not in self.KEYS:
                self.KEYS.add(tile)
        elif tile.isupper():
            if tile.lower() not in self.KEYS:
                doors[tile].append((r, c))
                return
        q.append((r, c))

    def collect_targets(self):
        while True:
            visited = [[False] * self.W for _ in range(self.H)]
            q = deque()
            doors = defaultdict(list)
            new_key_found = False

            for r in range(self.H):
                self.try_add(visited, q, doors, r, 0)
                self.try_add(visited, q, doors, r, self.W - 1)
            for c in range(self.W):
                self.try_add(visited, q, doors, 0, c)
                self.try_add(visited, q, doors, self.H - 1, c)

            dys = [-1, 0, 1, 0]
            dxs = [0, 1, 0, -1]
            while q:
                cy, cx = q.popleft()
                for dy, dx in zip(dys, dxs):
                    ny, nx = cy + dy, cx + dx
                    if not self.__in_range(ny, nx) or visited[ny][nx]:
                        continue
                    tile = self.GRID[ny][nx]
                    if tile == '*':
                        continue
                    visited[ny][nx] = True

                    if tile == '$':
                        self.RESULT += 1
                        self.GRID[ny][nx] = '.'
                        q.append((ny, nx))
                    elif tile == '.':
                        q.append((ny, nx))
                    elif tile.islower():  # key
                        if tile not in self.KEYS:
                            self.KEYS.add(tile)
                            new_key_found = True
                            door = tile.upper()
                            for r, c in doors[door]:
                                if not visited[r][c]:
                                    visited[r][c] = True
                                    q.append((r, c))
                            doors[door].clear()
                        q.append((ny, nx))
                    elif tile.isupper():  # door
                        if tile.lower() in self.KEYS:
                            q.append((ny, nx))
                        else:
                            doors[tile].append((ny, nx))
            if not new_key_found:
                break

    def result(self):
        return self.RESULT


if __name__ == "__main__":
    # 1. T cases are given.
    # 2. Each case contains a H*W grid and keys to open the corresponding doors.
    # 3. The letters in a grid represent:
    #       '.' empty space
    #       '*' wall
    #       '$' target
    #       'A ... Z' door
    #       'a ... z' key
    # 4. The goal is to take as many targets as possible.
    # 5. If I've got no keys, 0 will be given instead of lowercase alphabet keys.
    # 6. Begin from out of the grid, one can enter through empty spaces.
    # 7. Keys can be reused.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 2 <= H, W <= 10^2

    # Approach
    # 1. A BFS problem.
    # 2. visit check.
    # 3. Manage door encounters with a hashmap, so that obtained keys can be matched in O(1).
    # 4. It will take O(N^2) = O(10^4) < 1000ms per each case.

    t = int(input())
    for _ in range(t):
        stage = Stage()
        stage.collect_targets()
        print(stage.result())
