import sys

input = sys.stdin.readline


def backtrack(n, m, selected, subsets) -> None:
    # TC = O(N^M): each M positions can take N values
    # SC = O(M): call stack depth is M

    if len(selected) == m:
        subsets.append([*selected])
        return

    for i in range(1, n + 1):
        selected.append(i)
        backtrack(n, m, selected, subsets)
        selected.pop()


def find_valid_subsets(n: int, m: int) -> list[list[int]]:
    subsets = []
    backtrack(n, m, [], subsets)

    return subsets


if __name__ == "__main__":
    # With given natural numbers n, m,
    # find all the m length sequences that statisfy conditions below:
    # 1. Pick m numbers from range(1, n+1)
    # 2. Numbers can be selected for multiple times

    # The range of n and m is (1 <= m <= n <= 7)
    # Because the upper bound is small, typical backtracking would suffice

    # I solved this problem with two approaches:
    # 1. Print each result on the fly, returning nothing(32412kb, 1872ms)
    # 2. Append all the results in a subsets array and print them at the end(143376, 2672ms)
    # While the second approach is much tidier, the first one is more efficient.

    n, m = map(int, input().split())
    results = find_valid_subsets(n, m)

    for result in results:
        print(*result)
