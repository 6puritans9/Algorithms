def find_alarm_time(h: int, m: int) -> tuple[int, int]:
    # TC = O(1)
    # SC = O(1)

    if m >= 45:
        return h, m - 45

    return (h - 1) % 24, (m - 45) % 60


if __name__ == "__main__":
    # With given hour h and minute m, find the time 45 minutes before it

    # if m >= 45, return h and m - 45
    # if m < 45, return (h - 1) % 24 and (m - 45) % 60

    h, m = map(int, input().split())
    print(*find_alarm_time(h, m))
