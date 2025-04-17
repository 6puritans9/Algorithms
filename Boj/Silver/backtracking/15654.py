import sys

input = sys.stdin.readline


def backtrack(n, max_len: int, numbers: list[int], selected: list[int], visited: list[bool]):
    # TC = O(N^M)
    # SC = O(N)

    if len(selected) == max_len:
        print(" ".join(map(str, selected)))
        return

    for i in range(n):
        if not visited[i]:
            selected.append(numbers[i])
            visited[i] = True
            backtrack(n, max_len, numbers, selected, visited)
            selected.pop()
            visited[i] = False


def print_sequences(n: int, m: int, numbers: list[int]) -> None:
    visited = [False for _ in range(n)]

    backtrack(n, m, numbers, [], visited)


if __name__ == "__main__":
    # 1. From given N numbers of natural numbers,
    #   choose M numbers that make a sequence.
    # 2. The sequence should be in ascending order.
    # 3. Make no duplicates.

    # Constraints
    # TIME 1000ms
    # SPACE 512MB
    # 1. 1 <= M <= N <= 8
    # 2. 1 <= number <= 10^4

    # Approach
    # 1. Naive backtracking will suffice O(8^8)
    # 2. Sort the given numbers in ascending order
    # 3. Implement a permutation backtracking

    n, m = map(int, input().split())
    numbers = [int(num) for num in input().split()]
    numbers.sort()

    print_sequences(n, m, numbers)
