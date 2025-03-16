import sys

input = sys.stdin.readline


def print_seq(n: int, m: int, start: int, seq: list[int]):
    # TC = O(Comb(n + m - 1, m)) = O((n + m - 1)! / (m! * (n - 1)!))
    # SC = O(m)

    if len(seq) == m:
        print(*seq)
        return
    if start == n + 1:
        return

    for i in range(start, n + 1):
        seq.append(i)
        print_seq(n, m, i, seq)
        seq.pop()


if __name__ == "__main__":
    # With given integers n, m, find all the sequences that have length m
    # 1 <= m <= n <= 8
    # Numbers can be selected multiple times
    # Each sequence must be in ascending order( a1 <= a2 <= ... <= an)

    # Print appropriate sequences in each line with no duplicates
    # Blank space between numbers needed

    # This question asks to pick m choices from (n-1) + m possibilities
    # which is a variant of the stars and bars problem
    # Thus, the number of ways to do this corresponds to the combination formula:
    # O(combinations(n+m-1, m)) time
    # Due to the variant form of each sequence,
    # recursive backtracking is an efficient approach.

    n, m = map(int, input().split())
    print_seq(n, m, 1, [])
