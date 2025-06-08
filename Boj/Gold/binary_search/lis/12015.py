import sys

input = sys.stdin.readline


def search_leftmost_idx(lis: list[int, ...], target: int) -> int:
    left, right = 0, len(lis)

    while left < right:
        mid = (left + right) // 2

        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def find_len_subseq(n: int, seq: tuple[int, ...]) -> int:
    # TC = O(NlogN)
    # SC = O(N)

    lis = []
    for number in seq:
        insert_order = search_leftmost_idx(lis, number)

        if insert_order == len(lis):
            lis.append(number)
        else:
            lis[insert_order] = number

    return len(lis)


if __name__ == "__main__":
    # 1. For given sequence A,
    # 2. Find the length of the longest increasing subsequence.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 1 <= N <= 10^6
    # 2. 1 <= element <= 10^6

    # Approach
    # 1. This problem asks O(N) solution.
    # 2. A best practice to solve this problem will be
    #       using binary search O(logN),
    #       to find the best fit for iterating the sequence O(N)
    #       which will take O(NlogN) == O(N).
    # 3. Implement a binary search function
    #       that returns the idx that each number in the longest increasing sequence(lis) can be inserted.
    # 4. lis = []
    # 5. If index == len(lis): # biggest element inserted at tail
    #       append(element)
    #    else:
    #       replace lis[idx] with the current element to keep the lis as less value as possible.
    # 6. To visualize the given sequence (10, 20, 10, 30, 20, 50}:
    #       lis = [10]
    #       lis = [10, 20]
    #       lis = [10, 20] (10 is replaced with 10)
    #       lis = [10, 20, 30]
    #       lis = [10, 20, 30] (20 is replaced with 20)
    #       lis = [10, 20, 30, 50]
    # 7. return len(lis)

    n = int(input())
    seq = tuple(map(int, input().split()))

    print(find_len_subseq(n, seq))
