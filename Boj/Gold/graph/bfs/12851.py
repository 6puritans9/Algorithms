import sys
from collections import deque

input = sys.stdin.readline
LIMIT = 10 ** 5


def find_result(start: int, target: int) -> tuple[int, int]:
    # TC = O(10**5)
    # SC = O(10**5)

    if target <= start:
        return start - target, 1

    # 1. Initialize min_sec = sys.maxsize, count = 0
    # 2. From the starting point i, enqueue (i-1), (i+1), (2i) for each step as (sec, count)
    # 3. If i == target and min_sec > popped_sec:
    #       a. min_sec = sec
    #       b. count = 1
    # 4. elif i == target and min_sec == popped_sec:
    #       a. count += 1
    # 5. Traverse all the node will take O(10**5) < 2000ms

    dist = [-1 for _ in range(LIMIT + 1)]
    ways = [0 for _ in range(LIMIT + 1)]
    queue = deque([start])

    dist[start] = 0
    ways[start] = 1

    while queue:
        cur = queue.popleft()

        if dist[target] != -1 and dist[cur] > dist[target]:
            break

        sec = dist[cur] + 1
        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt <= LIMIT:
                if dist[nxt] == -1:
                    dist[nxt] = sec
                    ways[nxt] = ways[cur]
                    queue.append(nxt)
                elif dist[nxt] == sec:
                    ways[nxt] += ways[cur]

    return dist[target], ways[target]


if __name__ == "__main__":
    # 1. X, Y are playing hide-and-seek.
    # 2. X is on N, Y is on K
    # 3. X can walk or warp.
    #       a. if X walks for 1 sec, he will be on X-1 or X+1
    #       b. if X warps, he will be on 2*X after 1 sec
    # 4. Find the shortest time X can get Y,
    # 5. also find the number of ways that X find Y.

    # Constraints
    # TIME 2000ms
    # SPACE 512MB
    # 1. 0 <= N <= 10^5
    # 2. 0 <= K <= 10^5

    # Approach
    # 1. x, y can only be among (0<=N<=10^5)
    # 2. If y < x, x can only walk to y.
    #   a. shortest time = x-y
    #   b. shortest dist = x-y
    # 3. If x < y, this could be a dp problem.
    # 4. dp = [sys.maxsize * LIMIT + 1]
    # 5. dp[n]=0
    # 6. for i in range(n-1, -1, -1):
    #       dp[i] = dp[i+1] + 1
    # 7. for i in range(n, LIMIT + 1):
    #       if i % 2 == 0 and dp[i//2] != sys.maxsize:
    #           dp[i] = min(dp[i], dp[i//2] + 1)
    #       if i-1 >= 0 and dp[i-1] != sys.maxsize:
    #           dp[i] = min(dp[i], dp[i-1] + 1)
    #       if i+1 <= LIMIT and dp[i+1] != sys.maxsize:
    #           dp[i] = min(dp[i], dp[i+1] + 1)
    # 8. Dp is not valid because the solution requires backtracking

    # 1. Initialize min_sec = sys.maxsize, count = 0
    # 2. From the starting point i, enqueue (i-1), (i+1), (2i) for each step as (sec, count)
    # 3. If i == target and min_sec > popped_sec:
    #       a. min_sec = sec
    #       b. count = 1
    # 4. elif i == target and min_sec == popped_sec:
    #       a. count += 1
    # 5. Traverse all the node will take O(10**5) < 2000ms
    # 6. Initial solution needs pruning:
    #       a. check visited

    n, k = [int(num) for num in input().split()]
    result = find_result(n, k)
    print(*result, sep="\n")
