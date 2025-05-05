import sys

input = sys.stdin.readline


def find_optimal_solutions(n: int, solutions: list[int]) -> tuple[int, int]:
    # TC = O(N)
    # SC = O(1)

    left, right = 0, n - 1
    closest = float("inf")
    pairs = (None, None)

    while left < right:
        cur_sum = solutions[left] + solutions[right]

        if abs(cur_sum) < closest:
            closest = abs(cur_sum)
            pairs = (solutions[left], solutions[right])

        if cur_sum < 0:
            left += 1
        else:
            right -= 1

    return pairs


if __name__ == "__main__":
    # 1. There are two kind of solutions.
    # 2. Each solution has an integer which represents itself.
    # 3.  1 to 10^9 represents alkali,
    #    -1 to -10^9 represents acid.
    # 4. Integers are given in sorted order.
    # 5. Find the pair of solutions that makes the sum is closest to 0.
    # 6. If there are multiple pairs that makes the same sum, choose any.

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 2 <= N <= 10^5
    # 2. -10^9 <= integer <= 10^9

    # Approach
    # 1. Nested loop is not feasible O(10^10).
    # 2. As the input is given in sorted order,
    #       two pointers will solve this in O(N)
    # 3. left=0, right=n-1
    # 4. Begin with closest = float("inf")
    # 5. cur_sum = numbers[left] + numbers[right]
    # 6. while left < right:
    #    if abs(cur_sum) < closest:
    #       closest = abs(cur_sum)
    #       pair = (numbers[left], numbers[right])
    # 7. if cur_sum <0:
    #       left += 1
    #    else:
    #       right -= 1

    n = int(input())
    solutions = [int(num) for num in input().split()]

    result = find_optimal_solutions(n, solutions)
    print(" ".join(map(str, result)))
