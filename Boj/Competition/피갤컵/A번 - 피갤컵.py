def find_nth_competition(n: int) -> tuple[int, int]:
    STARTING_Y = 2024
    STARTING_M = 8
    interval = 7

    nxt_y = STARTING_Y + ((STARTING_M + interval * n - 1) // 12)
    nxt_m = (STARTING_M + interval * n - 1) % 12 + 1

    return nxt_y, nxt_m


if __name__ == "__main__":
    n = int(input())
    print(*find_nth_competition(n - 1))
