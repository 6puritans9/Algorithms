import sys

input = sys.stdin.readline


def find_min_subseq_len(n: int, s: int, seq: list[int]) -> int:
    # TC = O(N)
    # SC = O(1)

    min_len = float("inf")
    left, right = 0, 0
    cur_sum = 0

    while right < n:
        cur_sum += seq[right]

        while cur_sum >= s:
            min_len = min(min_len, right - left + 1)
            cur_sum -= seq[left]
            left += 1

        right += 1

    return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    # 1. N-length sequence is given.
    # 2. Find the minimum length of subsequence,
    #       which makes sum of greater or equal than S.

    # Constraints
    # TIME 500ms
    # SPACE 128MB
    # 1. 10^1 <= N < 10^5
    # 2. 0 < S <= 10^8

    # Approach
    # 1. This is a two-pointer problem
    # 2. Begin with i = 0, j = 1,
    #       cur_sum = seq[i] + seq[j]
    #       if cur_sum < S:
    #           j+=1
    #       else:
    #           min_len = min(min_len, j-i+1)
    #           i+=1
    # 3. This will take O(N) time, which is O(10^5) < 0.5 * 10^8

    n, s = map(int, input().split())
    sequence = [int(num) for num in input().split()]
    print(find_min_subseq_len(n, s, sequence))
