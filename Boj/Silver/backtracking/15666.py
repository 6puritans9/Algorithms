import sys

input = sys.stdin.readline


def backtrack(n, m, numbers, start: int, selected: list[int], printed: set):
    # TC = O(N^M)
    # SC = O(N^M)

    if len(selected) == m:
        key = tuple(selected)
        if key not in printed:
            printed.add(key)
            print(" ".join(map(str, selected)))
        return

    for i in range(start, n):
        selected.append(numbers[i])
        backtrack(n, m, numbers, i, selected, printed)
        selected.pop()


def print_sequences(n, m, numbers: list[int]):
    backtrack(n, m, numbers, 0, [], set())


if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = [int(num) for num in input().split()]
    numbers.sort()

    print_sequences(n, m, numbers)
