import sys

input = sys.stdin.readline


def find_max_score(n: int, steps: tuple[int, ...]) -> int:
    # TC = O(N)
    # SC = O(N)

    dp = [0 for _ in range(n + 1)]
    dp[1] = steps[1]

    if n > 1:
        dp[2] = steps[1] + steps[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + steps[i - 1]) + steps[i]

    return dp[n]


if __name__ == "__main__":
    # 1. Steps with scores are given.
    # 2. I can climb either 1 step or 2 steps.
    # 3. I cannot climb 3 consecutive steps.
    # 4. The destination is the last step.
    # 5. Find the maximum sum of steps achievable.

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 0 < Steps <= 300
    # 2. 0 < steps <= 10^4

    # Approach
    # 1. There are two possibilities:
    #       climb a single step or jump 2 steps.
    # 2. The tricky part is managing the state of climbing 3 consecutive steps.
    # 3. which can be described as follows:
    #       - dp[i-2] + steps[i] as a jump
    #       - from the base state dp[i-3],
    #           jump to steps[i-1]:
    #           and climb one additional step, which is steps[i].

    n = int(input())
    steps = (0,) + tuple(int(input()) for _ in range(n))

    print(find_max_score(n, steps))
