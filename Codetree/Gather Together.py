# Back to Exhaustive Search, because I'm having problems with dynamic programming problems
# and advanced exhaustive search problems.

def find_min_movs(n, people):
    min_movs = float("inf")

    for i in range(1, n + 1):
        cur_movs = 0

        for j, person in enumerate(people):
            cur_movs += abs(j - i) * person

        min_movs = min(min_movs, cur_movs)

    return min_movs


if __name__ == "__main__":
    n = int(input())
    people = [0, *(int(num) for num in input().split())]

    print(find_min_movs(n, people))