import sys

input = sys.stdin.readline


def find_min_count(a: int, b: int) -> int:
    # TC = O(logN)
    # SC = O(1)

    count = 1

    while b > a:
        if b % 2 == 0:
            b //= 2
        elif b % 10 == 1:
            b //= 10
        else:
            return -1

        count += 1

    return count if b == a else -1


# Takes too much time
# def backtrack(a, b, count: int) -> int:
#     # TC = O(2^N)
#     # SC = O(1)
#
#     if a == b:
#         return count
#     if a > b or len(str(a)) > len(str(b)):
#         return -1
#
#     result1 = backtrack(a * 2, b, count + 1)
#     result2 = backtrack(int(str(a) + '1'), b, count + 1)
#
#     if result1 == -1 and result2 == -1:
#         return -1
#     if result1 == -1:
#         return result2
#     if result2 == -1:
#         return result1
#
#     return min(result1, result2)


if __name__ == "__main__":
    # 1. Integers A and B are given.
    # 2. To convert A to B, two operations are valid.
    #       a. multiply 2
    #       b. append 1 to the rightmost
    # 3. Find the minimum count of operations.
    # 4. If it is not possible, print -1.

    # Constraints
    # TIME 2000ms
    # SPACE 512MB
    # 1. 1 <= A < B <= 10^9

    # Approach
    # 1. Two options are available for each step.
    # 2. a *= 2 or a = int(str(a) + '1')
    # 3. Pass 'a' recursively until a == b.
    # 4. if a == b:
    #       return count
    # 3. if a > b or len(str(a)) > len(str(b):
    #       return

    a, b = map(int, input().split())

    result = find_min_count(a, b)
    print(result if result else -1)
