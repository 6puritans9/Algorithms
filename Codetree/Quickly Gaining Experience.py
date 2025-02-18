# Initial solution, which works but is not efficient enough.

def find_min_time(quests, m) -> int:
    EXP_LIMIT = 1000000

    dp = [float("inf")] * (EXP_LIMIT + 1)
    dp[0] = 0

    for exp, time in quests:
        for i in range(EXP_LIMIT, exp - 1, -1):
            dp[i] = min(dp[i], dp[i - exp] + time)

    answer = float("inf")
    for i in range(m, EXP_LIMIT):
        answer = min(answer, dp[i])
    return answer if answer != float("inf") else -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    quests = []
    for _ in range(n):
        exp, time = map(int, input().split())
        quests.append((exp, time))

    print(find_min_time(n, quests, m))
