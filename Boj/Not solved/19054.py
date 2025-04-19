# This problem cannot be solved with greedy approach
# I need to find the optimal solution with memoization
# not to exceed the recursion depth limit.

import sys
from collections import deque

input = sys.stdin.readline


class Game:
    def __init__(self, seq: deque[int]):
        self.players = [0, 0]

    def __add_xor_sum(self, player, value: int) -> None:
        self.players[player] = value

    def __xor_sum(self, player: int, value: int) -> int:
        return self.players[player] ^ value

    def __choose_either(self, player, seq) -> (bool, int):
        begin_sum = self.__xor_sum(player, seq[0])
        end_sum = self.__xor_sum(player, seq[-1])

        if begin_sum >= end_sum:
            return True, begin_sum
        else:
            return False, end_sum

    def __turn(self, player: int, seq: deque[int]):
        is_first, xor_sum = self.__choose_either(player, seq)
        if is_first:  # pick the beginning
            self.__add_xor_sum(player, xor_sum)
            seq.popleft()
        else:  # pick the end
            self.__add_xor_sum(player, xor_sum)
            seq.pop()

    def play(self, seq: deque[int]):
        player = 0

        while len(seq):
            self.__turn(player, seq)
            player ^= 1

    def print(self):
        results = ("Draw", "First", "Second")
        idx = 0

        first = self.players[0]
        second = self.players[1]
        if first > second:
            idx = 1
        elif second > first:
            idx = 2

        print(results[idx])


# if __name__ == "__main__":
#     # 1. Two players play a game for T rounds
#     # 2. Each game has a sequence of N integers
#     # 3. Players choose a number either at the beginning or at the end in turn,
#     #       and add the value to an XOR sum,
#     #       which start from 0 initially.
#     # 4. The round ends when the sequence is empty.
#     # 5. The player with highest XOR sum wins.
#     # 6. Print "First" | "Second" | "Draw" according to the result.
#
#     # Constraints
#     # TIME 1000ms
#     # SPACE 256MB
#     # 1. 1 <= T <= 12
#     # 2. 1 <= N <= 5*10^4
#     # 3. 1 <= X <= 10^9
#
#     # Approach
#     # 1. This will take time O(T * N) = O(12 * (5*10^4))
#     #       XOR will take O(10^9) length in binary
#     # 2. Pop one of either values that maximize the current player's XOR sum
#     #       which requires deque
#     # 3. if not len(seq): compare and print(result)
#
#     # TC = O(TN)
#     # SC = O(1)
#
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         sequence = deque([int(num) for num in input().split()])
#         game = Game(sequence)
#
#         game.play(sequence)
#         game.print()
