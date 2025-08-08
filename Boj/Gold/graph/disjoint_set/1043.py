import sys
from collections import deque

input = sys.stdin.readline


def find(x: int, parent: list[int]) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x], parent)

    return parent[x]


def union(x: int, y: int, parent: list[int]) -> None:
    root_x = find(x, parent)
    root_y = find(y, parent)

    if root_x != root_y:
        parent[root_y] = root_x


def find_max_parties(n: int, unmaskers: list[int], parties: deque[tuple[int, ...]]) -> int:
    # TC = O(MN)
    # SC = O(N)

    parent = [i for i in range(n + 1)]

    for party in parties:
        base = party[0]

        for attendee in party[1:]:
            union(base, attendee, parent)

    truth_roots = set(find(u, parent) for u in unmaskers)

    result = 0
    for party in parties:
        if not any(find(attendee, parent) in truth_roots for attendee in party):
            result += 1

    return result


if __name__ == "__main__":
    # 1. The number of people N, and the number of parties I should attend M is given.
    # 2. I can lie or I can tell the truth.
    # 3. The number of people who know the truth is given in the second line.
    #       a. and I have to tell the truth in the parties they attend.
    # 4. If I lied to someone before, but they attend another party with them, lies will reveal.
    # 5. Find the possible number of parties that I keep the lie.

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= N, M <= 50

    # Approach
    # 1. Add truth-finders into a queue.
    # 2. Enqueue or push all the parties into a deque.
    # 3. Iterate the parties that the truth-finders are included.
    # 4. Enqueue other people who attended the same party as truth-finders.
    #   a. while managing the dequeued people with a visited list.
    # 5. if not queue:
    #       return len(queue)
    # 6. Or, I can solve it with union-find.

    n, m = map(int, input().split())
    unmaskers = [int(num) for num in input().split()[1:]]
    parties = deque([tuple(int(num) for num in input().split()[1:]) for _ in range(m)])

    print(find_max_parties(n, unmaskers, parties))
