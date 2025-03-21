import sys

input = sys.stdin.readline


def find_min_subarray_len(n: int, k: int, dolls: list[int]) -> int:
    # TC = O(N)
    # SC = O(1)

    min_len = float("inf")
    left = 0
    lions = 0

    for right in range(n):
        if dolls[right] == 1:
            lions += 1

        while lions >= k:
            min_len = min(min_len, right - left + 1)

            if dolls[left] == 1:
                lions -= 1
            left += 1

    return min_len if min_len != float("inf") else -1


if __name__ == "__main__":
    # N dolls are given(1 for lion, 2 for peach)
    # Find the minimum length of continuous subarray,
    # which contains greater or equal than k number of 1

    # Constraints:
    # 1 <= K, N <= 10^6
    # time <= 1000ms
    # memory <= 256MB

    # As N <= 10^6, O(N^2) cannot meet the time limit
    # By using sliding_window, it can be solved just in one iteration O(N)

    n, k = map(int, input().split())
    dolls = [int(num) for num in input().split()]

    print(find_min_subarray_len(n, k, dolls))
