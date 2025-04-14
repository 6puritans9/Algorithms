from collections import deque


def is_valid(speed: int):
    return speed > 0


def bfs(x: int, initial_state: tuple[int]) -> int:
    # TC = O(MAX_BOUNDARY^2) = O(X^2) = O(10^8) == 1000ms
    # SC = O(X^2) = O(10^8) = 1bytes *10^2 * (10^3)^2  == 100MB

    MAX_DIST = 2 * x
    MAX_SPEED = 100

    queue = deque([initial_state])
    visited = [[False for _ in range(MAX_SPEED)] for _ in range(MAX_DIST)]

    while queue:
        dist, speed, time = queue.popleft()
        if dist == x and speed == 1:
            return time + 1

        if dist >= MAX_DIST or speed >= MAX_SPEED:
            continue
        if visited[dist][speed]:
            continue
        visited[dist][speed] = True

        if is_valid(speed - 1):
            queue.append((dist + speed, speed - 1, time + 1))
        queue.append((dist + speed, speed, time + 1))
        queue.append((dist + speed, speed + 1, time + 1))

    return -1


def find_min_time(x: int) -> int:
    initial_state = (0, 1, 0)

    return bfs(x, initial_state)


if __name__ == "__main__":
    # 1. Going to run for X length
    # 2. Start from 1m/s, for every 1 sec, a decision should be made
    #   +1m/s or -1m/s or +0m/s
    # 3. The speed has to be 1m/s at the destination
    # 4. Speed cannot be 0m/s
    # 5. Find the minimum time to reach the destination

    # Constratins
    # Time 5000ms
    # Space 288MiB
    # 1 <= X <= 10^4

    # Approach
    # 1. Backtracking is not feasible due to its tc O(2^x)
    # 2. Set a state (cur_dist, cur_speed) for each step
    #       The final state should be (x, 1)
    # 3. From each state, I can make transition to:
    #       (cur_dist + 1, cur_speed + 1)
    #       (cur_dist + 1, cur_speed - 1)
    #       if cur_speed <=0:
    #           return
    # 4. Use visited to avoid cycles
    # 5. BFS

    x = int(input())
    print(find_min_time(x))