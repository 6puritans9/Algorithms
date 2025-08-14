import bisect
import sys

input = sys.stdin.readline


# TC = O(MlogM) == O(4*10^6) <= 1200ms
# SC = O(M)


class DisjointSet:
    # TC = O(a(N))
    # SC = O(M)
    def __init__(self, len_deck: int):
        self.parent = [i for i in range(len_deck + 1)]

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        # union x to y
        self.parent[self.find(x)] = self.find(y)


class Game:
    def __init__(self):
        # TC = O(MlogM)
        self.n, self.m, self.k = map(int, input().split())
        self.deck = sorted([int(num) for num in input().split()])
        self.a_orders = [int(num) for num in input().split()]
        self.ds = DisjointSet(self.m)

    def play(self):
        # TC = O(KlogM)
        for order in self.a_orders:
            idx = bisect.bisect_right(self.deck, order)
            idx = self.ds.find(idx)

            if idx >= self.m:
                idx = self.ds.find(0)

            print(self.deck[idx])
            self.ds.union(idx, idx + 1)


if __name__ == "__main__":
    # 1. This is a card game with following rules.
    # 2. There are N red cards, each has a distinct number in range(1, N+1).
    #       Choose M cards from here.
    # 3. N blue cards are there, each has a distinct number in range(1, N+1).
    #       Choose M cards from here which is same as the selected red ones.
    # 4. A holds the red, B holds the blue.
    # 5. A and B submit one of the selected cards.
    #       The bigger number wins, and they cannot be used again.
    # 7. Repeat this for K times.
    # 8. People with more wins take the game.

    # 9. A has an ability that can manipulate his cards.
    #       a. He can submit the card that is already been submitted.
    #       b. He can submit the card that B doesn't have.
    # 10. B can detect which card that A will submit.
    #       a. So he can submit the lowest card which is larger than A submitted.
    # 11. The input is given as the instruction:
    #       a. N, M, K is given in the first line.
    #       b. M numbers are given. each number represents the number of a card. all the numbers are distinct.
    #       c. K numbers are given. each number represents the card that A submits.
    # 12. Print the card that B will submit in each line.

    # Constraints
    # TIME 1200ms
    # SPACE 512MB
    # 1. 1 <= M <= N <= 4 * 10^6
    # 2. 1 <= K <= min(M, 10^4)

    # Approach
    # 1. Sort the cards in asc order. O(NlogN) == O(10^6)
    # 2. There are cases:
    #       a. A submits the biggest number in the deck: B should hand the lowest number
    #       b. A submits a card less than the biggest: B hands the lowest number but bigger than A's
    # 3. So this problem asks to find the most time-effective approach.
    # 4. With naive approach:
    #       O(N) search for M times = O(NM) = O(N^2) > 1200ms
    # 5. with binary search:
    #       O(MlogN) == O(M)
    # 6. Mark used state with bitmasking.
    # >> Proven to be not efficient for 4*10^6

    # 1. Manage the connection and used state and with a disjoint set. O(a(N))
    # 2. For the case A, handle it to find from idx 0.

    game = Game()
    game.play()

# Bisect with Bitmasking
# class Game:
#     def __init__(self):
#         self.n, self.m, self.k = map(int, input().split())
#         self.deck = [int(num) for num in input().split()]
#         self.a_orders = [int(num) for num in input().split()]
#
#     def show(self, value: int):
#         print(value)
#
#     def prepare(self):
#         self.deck.sort()
#
#     def play(self):
#         used = 0
#
#         for order in self.a_orders:
#             # case A
#             if order == self.deck[-1]:
#                 found = False
#                 b_idx = 0
#                 while not found:
#                     b_idx = bisect.bisect_right(self.deck, self.deck[0], b_idx, self.m)
#                     if used & (1 << b_idx):
#                         continue
#                     found = True
#                     used |= (1 << b_idx)
#                 continue
#
#             # case B
#             found = False
#             b_idx = 0
#             while not found:
#                 b_idx = bisect.bisect_right(self.deck, order, b_idx, self.m)
#                 if used & (1 << b_idx):
#                     continue
#                 found = True
#                 used |= (1 << b_idx)
#
#             self.show(self.deck[b_idx])
