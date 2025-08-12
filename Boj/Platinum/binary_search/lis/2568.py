import sys
import bisect

input = sys.stdin.readline


def find_overlapping_wires(n: int, connections: list[tuple[int, ...]]) -> list[int]:
    # TC = O(NlogN)
    # SC = O(N)

    lis = []
    lis_idx = []
    prv = [-1 for _ in range(n)]

    b_nodes = [connections[i][1] for i in range(n)]
    for i, val in enumerate(b_nodes):
        pos = bisect.bisect_left(lis, val)
        if pos == len(lis):
            lis.append(val)
            lis_idx.append(i)
        else:
            lis[pos] = val
            lis_idx[pos] = i
        if pos > 0:
            prv[i] = lis_idx[pos - 1]

    lis_path = []
    curr = lis_idx[-1]
    while curr != -1:
        lis_path.append(curr)
        curr = prv[curr]

    lis_set = set(lis_path)
    removed = [connections[i][0] for i in range(n) if i not in lis_set]

    return removed


if __name__ == "__main__":
    # 1. There are two telephone poles with N segments.
    # 2. Some segments are connected with wires.
    # 3. The goal is to get rid of the intertwined
    #    by removing some of the wires.
    # 4. Find the minimum number of wires that meets the goal.
    # 5. Print the result in the given order:
    #       a. The number of wires
    #       b. Each connected segment A

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 1 <= N <= 10^5
    # 2. 1 <= segment <= 5 * 10^5
    # 3. A segment can have only one line.

    # Approach
    # 1. Sort the connections by A. O(NlogN)
    # 2. Extract B values from the sorted connections.
    # 3. Find the LIS in B using binary search. O(NlogN)
    # 4. Determine which wires are part of the LIS and which are not(remove).
    # 5. Output:
    #       a. Number of wires removed = N - len(LIS)
    #       b. The A values of removed wires in asc order.

    n = int(input())
    connections = [tuple(int(num) for num in input().split()) for _ in range(n)]
    connections.sort(key=lambda x: (x[0], x[1]))

    result = find_overlapping_wires(n, connections)
    print(len(result))
    print(*result, sep="\n")
