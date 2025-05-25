import sys

input = sys.stdin.readline


def cost(curr_pos: int, next_pos: int) -> int:
    if not curr_pos:
        return 2

    elif curr_pos == next_pos:
        return 1

    elif abs(curr_pos - next_pos) == 2:
        return 4

    else:
        return 3


def min_cost(seq: list[int]) -> int:
    # TC = O(N)
    # SC = O(N)

    n = len(seq)
    dp = [[[float("inf") for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        next_pos = seq[i - 1]

        for left in range(5):
            for right in range(5):
                if dp[i - 1][left][right] == float("inf"):
                    continue

                # Move left foot to next_pos
                if next_pos != right:
                    dp[i][next_pos][right] = min(dp[i][next_pos][right], dp[i - 1][left][right] + cost(left, next_pos))

                # Move right foot to next_pos
                if next_pos != left:
                    dp[i][left][next_pos] = min(dp[i][left][next_pos], dp[i - 1][left][right] + cost(right, next_pos))

    result = float("inf")
    for left in range(5):
        for right in range(5):
            result = min(result, dp[n][left][right])

    return result


if __name__ == "__main__":
    # 1. This is a game consists of four arrows.
    # 2. 1 for north, 2 for west, 3 for south, 4 for east, 0 for the center which is the starting point.
    # 3. A gamer can only step on one arrow with his one foot,
    #       and he cannot move both feet simultaneously.
    # 4. Each route has its own cost:
    #       from 0 to 1 | 2 | 3 | 4 takes two.
    #       from 1 | 2 | 3 | 4 to the same arrow takes one.
    #       from 1 | 2 | 3 | 4 to other arrows takes three.
    #       from 1 | 2 | 3 | 4 to the opposite arrow takes four.
    # 5. For example, (0,0) >> (0,1) >> (2,1) >> (2,1) >> (2,4) takes minimum cost of 8.
    # 6. Find the minimum cost for the given input.

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. len(seq) <= 10^5
    # 2. each element is in (1, 2, 3, 4)
    # 3. 0 marks the end of input

    # Approach
    # 1. dp[left][right] = cost
    # 2. dp[0][0] = 0
    # 3. dp[0][1] = min(dp[0][1], dp[0][0] + 2)
    # 4. dp[0][2] = min(dp[0][2], dp[0][1] + 3, )
    #    dp[1][2] = dp[]...
    # 5. This is not feasible to manage the state.
    # 6. Also, I need an additional helper function to get the cost.

    # 7. This problem asks an exhaustive search after all.
    # 8. So every [left][right] state transition should be tracked and compared.
    # 9. For each step i,
    #       seq[i] = next_step
    #       dp[i][next_step][right] = dp[i-1][left][right] + cost(left, next_step)
    #       dp[i][left][next_step] = dp[i-1][left][right] + cost(right, next_step)
    # 10. Return the minimum cost in the dp[n] row.

    seq = [int(num) for num in input().split()]
    print(min_cost(seq[:-1]))
