import sys
input = sys.stdin.readline

def get_max_overlaps(n, starts, ends):
    events = []
    for i in range(n):
        events.append((starts[i], 1))
        events.append((ends[i], -1))
    events.sort()

    max_overlaps = 0
    active_intervals = 0
    for _, change in events:
        active_intervals += change
        max_overlaps = max(max_overlaps, active_intervals)

    return max_overlaps


if __name__ == "__main__":
    n = int(input())
    starts = []
    ends = []
    for _ in range(n):
        start, end = map(int, input().split())
        starts.append(start)
        ends.append(end)

    print(get_max_overlaps(n, starts, ends))
