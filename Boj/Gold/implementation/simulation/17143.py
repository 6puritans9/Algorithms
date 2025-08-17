import sys
from collections import defaultdict

input = sys.stdin.readline


# TC = O(C * {M * max(R, C)}) == O(10^2 * (10^4 * 10^2)) = O(10^8) >= 1000ms
# SC = O(M)


class Shark:
    def __init__(self, r: int, c: int, s: int, d: int, w: int):
        self.r = r
        self.c = c
        self.speed = s
        self._dir = d
        self.weight = w

    def move(self):
        global R, C
        if self._dir in (1, 2):  # vertical
            period = 2 * (R - 1)
            s = self.speed % period if period else 0  # compress the distance

            for _ in range(s):
                delta = -1 if self._dir == 1 else 1

                nr = self.r + delta
                if not (0 <= nr < R):
                    self.flip()
                    delta = -delta
                    nr = self.r + delta
                self.r = nr
        else:  # horizontal
            period = 2 * (C - 1)

            s = self.speed % period if period else 0
            for _ in range(s):
                delta = -1 if self._dir == 4 else 1

                nc = self.c + delta
                if not (0 <= nc < C):
                    self.flip()
                    delta = -delta
                    nc = self.c + delta
                self.c = nc

    def flip(self):
        self._dir = {1: 2, 2: 1, 3: 4, 4: 3}[self._dir]


class Fisherman:
    def __init__(self):
        self.pos = -1
        self.net = []

    def move(self):
        self.pos += 1

    def catch(self, ocean: dict[tuple[int, int], list]):
        global R

        # O(100)
        for r in range(R):
            cell = ocean[(r, self.pos)]
            if cell:
                shark = cell.pop()
                self.net.append(shark.weight)
                break


if __name__ == "__main__":
    # 1. A (R*C) sized grid is given that is 1-based index.
    # 2. Each cell can contain a shark which has size and velocity.
    # 3. Things move synchronously in seconds:
    #       a. A fisherman moves to i = (C + 1) from i = -1.
    #       b. He takes a shark that is the closest to row 0.
    #       c. Sharks move in their direction, until meet the boundary, which it flips.
    #       d. If two sharks collide after completing move, the bigger one consumes the smaller one.
    # 4. When the fisherman is out of bound, print the sum of all the sharks' weight.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 2 <= R, C <= 10^2
    # 2. 0 <= M <= R*C
    # 3. Shark:
    #       1 < = r <= R
    #       1 <= c <= C
    #       0 <= speed <= 10^3
    #       1 <= direction <= 4; 1=up, 2=down, 3=right, 4=left
    #       1 <= weight <= 10^4
    # 4. Each shark has distinct weight, no more than 2 sharks can be in the same cell.

    # Approach
    # 1. This is an implementation problem.
    # 2. Make a Shark class:
    #       a. fields: weight(int), velocity(int), direction(int), active(bool).
    #       b. methods: move(), consume(), flip().
    # 3. Make a Fisherman class:
    #       a. fields: pos(int), caught(List[Shark])
    #       b. methods: move(), catch()
    # 4. while(fisherman.pos < C):
    #       fisherman.move() >> fisherman.catch() >> sharks.move() >> sharks.consume()
    # 5. print(sum(fisherman.caught.weight))

    R, C, M = map(int, input().split())
    ocean: dict[tuple[int, int], list[Shark]] = defaultdict(list)

    fisherman = Fisherman()
    for _ in range(M):
        r, c, speed, direction, weight = map(int, input().split())

        # index base handling
        r -= 1
        c -= 1

        shark = Shark(r, c, speed, direction, weight)
        ocean[(r, c)].append(shark)

    while fisherman.pos < C:
        # fisherman acts first
        fisherman.move()
        fisherman.catch(ocean)

        new_ocean = defaultdict(list)
        # sharks acts next
        for (y, x), sharks in ocean.items():
            if sharks:
                shark = sharks[0]
                shark.move()
                ny, nx = shark.r, shark.c
                new_ocean[(ny, nx)].append(shark)

        # if two sharks collide, pop the smaller one
        for key, sharks in new_ocean.items():
            if len(sharks) > 1:
                biggest = max(sharks, key=lambda s: s.weight)
                new_ocean[key] = [biggest]

        ocean = new_ocean

    print(sum(fisherman.net))
