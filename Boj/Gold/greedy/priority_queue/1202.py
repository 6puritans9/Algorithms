import heapq
import sys

input = sys.stdin.readline


def find_max_value(n: int, gems: list[int], capacities: list[int]) -> int:
    # TC = O(NlogN)
    # SC = O(N)

    gems.sort(key=lambda x: x[0])  # sort by weight in asc order
    capacities.sort()  # sort in asc order

    max_value = 0
    heap = []
    i = 0

    for capacity in capacities:
        while i < n and gems[i][0] <= capacity:
            heapq.heappush(heap, -gems[i][1])
            i += 1

        if heap:
            max_value += -heapq.heappop(heap)

    return max_value


if __name__ == "__main__":
    # 1. There are N gems in a shop.
    # 2. Each gem weighs Mi while having value Vi.
    # 3. The thief has K bags which can hold weight Ci,
    # 4. But each bag can hold only 1 gem.
    # 5. Find the maximum value that the thief can take.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= N, K <= 3 * 10^5
    # 2. 0 <= Mi, Vi <= 10^6
    # 3. 1 <= Ci <= 10^8

    # Approach
    # 1. This is a knapsack problem with a twist.
    # 2. As O(10^5) is required to solve this problem, the time complexity should be O(N) or O(NlogN).
    # 3. Sort the (weight, value) pair by value in descending order. O(NlogN)
    # 4. Sort the capacities in ascending order. O(NlogN)
    # 5. taken = [False for _ in range(N)] << not needed
    # 6. Traversing capacities, store the gem state in the taken array. O(N) << not needed
    # 7. Use binary search to find the optimal fit. O(logN)
    # 8. Actually, using max heap is more efficient because it prunes the remaining gems automatically. O(NlogN)
    # 9. This will take O((N+K)logN).

    n, k = map(int, input().split())
    gems = []
    capacities = []
    for _ in range(n):
        m, v = map(int, input().split())
        gems.append((m, v))
    for _ in range(k):
        capacity = int(input())
        capacities.append(capacity)

    print(find_max_value(n, gems, capacities))
