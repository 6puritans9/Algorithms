import sys

input = sys.stdin.readline


# Total TC = O(NlogN)
# Total SC = O(1)

def find_max_meetings(n: int, meetings: list[int]) -> int:
    # TC = O(N)
    # SC = O(1)

    count = 1
    prv_end = meetings[0][1]

    for i in range(1, n):
        nxt_start, nxt_end = meetings[i]

        if nxt_start >= prv_end:
            count += 1
            prv_end = nxt_end

    return count


if __name__ == "__main__":
    # Problem
    # For a single meeting room,
    # With given N meetings (start, end),
    # Find the maximum number of meetings
    # which does not overlap.

    # 1. The next meeting can be held after previous meeting immediately,
    #       which means end1 == start2 is valid
    # 2. start1 == end1 is also valid

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1 <= N <= 10^5
    # 0 <= start <= end <= 2^31 - 1

    # Approach
    # 1. Sort the meetings by their end in ascending order O(NlogN)
    # 2. for i in range(n-1): O(N)
    #       if arr[i+1][1] >= end:
    #           count += 1
    #           end = arr[i+1][1]
    # 3. return count

    n = int(input())
    meetings = []
    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))
    meetings.sort(key=lambda x: (x[1], x[0]))

    print(find_max_meetings(n, meetings))
