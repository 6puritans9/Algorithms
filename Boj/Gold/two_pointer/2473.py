import sys

input = sys.stdin.readline


def optimal_mixture(n: int, solutions: list[int]) -> list[int]:
    closest = float('inf')
    answer = []

    for start in range(n - 2):
        left, right = start + 1, n - 1

        while left < right:
            mixture = solutions[start] + solutions[left] + solutions[right]
            if abs(mixture) < abs(closest):
                closest = mixture
                answer = [solutions[start], solutions[left], solutions[right]]
                if closest == 0:
                    return answer

            else:
                if mixture > 0:
                    right -= 1
                else:
                    left += 1

    return answer


# def optimal_mixture(n: int, solutions: list[int]) -> list[int]:
#     result = float("inf")
#     comb = []
#
#     start = 0
#     while start < n - 2:
#         left, right = start + 1, start + 2
#
#         while left < right < n:
#             mixture = solutions[start] + solutions[left] + solutions[right])
#             if abs(mixture) > abs(result):
#                 if mixture > 0:
#                     right += 1
#                 elif mixture < 0:
#                     left += 1
#             else:
#                 result = mixture
#                 comb = [solutions[start], solutions[left], solutions[right]]
#             if result == 0:
#                 return comb
#         start += 1
#
#     return comb


if __name__ == "__main__":
    # 1. There are acid and alkaline solutions in a lab.
    # 2. Acid values range from 1 to 10^9,
    #       alkaline range from -1 to -10^9.
    # 3. Mix three same amount of solutions to make a mixture that is closest to 0.
    # 4. Each solution is distinct and given in random order.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 3 <= N <= 5 * 10^3
    # 2. -10^9 <= solution <= 10^9

    # Approach
    # 1. If naively iterates in O(n^3), it exceeds the time limit. O(10^9)
    # 2. Using dp will take O(N^3) too.
    # 3. The thing is, to get the answer, all the numbers has to be iterated in the due time.
    # 4. So the only option is to reduce O(N^3) into something less.
    # 5. A probable approach is selecting an element from index 0, iterate n-1 elements using two-pointers
    #       to get the sum closest to zero.
    # 6. The input has to be sorted. O(nlogn)
    # 7. answer = float("inf")
    # 8. start = 0, left = start + 1, right = n - 1
    #       two pointers narrow down from both ends because the solutions are sorted in ascending order.
    # 9. if abs(sum(a,b,c)) < abs(answer): answer = sum(a,b,c)
    # 10. This will take O(N^2) = O(25 * 10^6) <= 1000ms

    n = int(input())
    solutions = [int(num) for num in input().split()]
    solutions.sort()
    result = optimal_mixture(n, solutions)
    print(" ".join(map(str, result)))
