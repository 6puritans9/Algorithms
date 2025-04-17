import sys

input = sys.stdin.readline


def backtrack(n: int, m: int, numbers: list[int], selected: list[int], visited: list[bool], printed):
    # TC = O(N^M)
    # SC = O(N) + O(N!/(N-M)!) == 4bytes * 8! < 512MB

    if len(selected) == m:
        key = tuple(selected)
        if key not in printed:
            printed.add(key)
            print(" ".join(map(str, selected)))
        return

    for i in range(n):
        if not visited[i]:
            selected.append(numbers[i])
            visited[i] = True
            backtrack(n, m, numbers, selected, visited, printed)
            selected.pop()
            visited[i] = False


def print_sequences(n: int, m: int, numbers: list[int]) -> None:
    visited = [False for _ in range(n)]

    backtrack(n, m, numbers, [], visited, set())


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
    # 2. The tricky part is handling duplicate given numbers
    # 3. Make an additional array to contain all the previous states
    # 4. Naive implementation of printed which consists of deep copied list is not time-efficient
    # 5. As python set is implemented as a hash table, utilizing it will achieve O(1) for lookup

    n, m = map(int, input().split())
    numbers = [int(num) for num in input().split()]
    numbers.sort()

    print_sequences(n, m, numbers)
