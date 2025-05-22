import sys

input = sys.stdin.readline


def find_primes(n: int) -> list[int]:
    # TC = O(N)
    # SC = O(N)

    sieve = [True for _ in range(n + 1)]
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)

    return primes


def find_combinations(n: int, primes: list[int]) -> int:
    # TC = O(N)
    # SC = O(1)

    if not primes:
        return 0

    combinations = 0
    left, right = 0, 0
    cur_sum = primes[0]

    while left < len(primes):
        if cur_sum == n:
            combinations += 1
            cur_sum -= primes[left]
            left += 1

        elif cur_sum < n and right < len(primes) - 1:
            right += 1
            cur_sum += primes[right]

        else:
            cur_sum -= primes[left]
            left += 1

    return combinations


if __name__ == "__main__":
    # 1. Some natural numbers can be represented as sum of consecutive prime numbers.
    # 2. For examples,
    #       a. 41: 2+3+5+7+11+13 or 11+13+17 or 41
    #       b. 53: 5+7+11+13+17 or 53
    # 3. These are not valid:
    #       a. 20: 7+13 because they are not consecutive
    #       b. 13: 3+5+5+7 because there are duplicates
    # 4. Find the number of valid combinations.

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= N <= 4 * 10^6

    # Approach
    # 1. Find the set of available prime numbers of N using Eratosthenes' sieve. O(N)
    # 2. Using two-pointers, find the number of possible combinations.

    n = int(input())
    primes = find_primes(n)
    print(find_combinations(n, primes))
