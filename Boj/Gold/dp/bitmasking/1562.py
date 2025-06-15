import sys

input = sys.stdin.readline

MOD = 10 ** 9


def every_stair_numbers(n: int) -> int:
    # TC = O(N * 2^10 * 10) == O(N)
    # SC = O(N * 2^10 * 10) = O(4bytes * 1024 * 10) == 40KB

    if n < 10:
        return 0

    # dp[length][last_digit][mask]
    dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(n + 1)]

    # Init
    # 1. length > 0
    # 2. the first digit cannot be 0
    for digit in range(1, 10):
        dp[1][digit][1 << digit] = 1

    for length in range(2, n + 1):
        for last_digit in range(10):
            for mask in range(1 << 10):
                count = dp[length - 1][last_digit][mask]
                if not count:
                    continue

                # if last_digit == 0: next_digit = last_digit + 1; if last_digit < 9
                # if last_digit == 9: next_digit = last_digit - 1; if last_digit > 0
                # both directions should be handled
                if last_digit > 0:
                    next_digit = last_digit - 1
                    dp[length][next_digit][mask | (1 << next_digit)] += count
                    dp[length][next_digit][mask | (1 << next_digit)] %= MOD

                if last_digit < 9:
                    next_digit = last_digit + 1
                    dp[length][next_digit][mask | (1 << next_digit)] += count
                    dp[length][next_digit][mask | (1 << next_digit)] %= MOD

    full_mask = (1 << 10) - 1
    result = 0
    for last_digit in range(10):
        result += dp[n][last_digit][full_mask]
        result %= MOD

    return result


if __name__ == "__main__":
    # 1. Suppose there's a number 45656.
    #       a. It has neighbouring digits of +-1.
    #       b. This is what we call a stair number.
    # 2. A natural number N is given.
    # 3. Find numbers which meet the following conditions:
    #       a. Length N
    #       b. Every number in range[0, 9] should appear
    # 4. Print (result % 10^9).
    # 5. Starting with 0 is not a stair number

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= N <= 100

    # Approach
    # 1. A naive approach will take O(10^100) which is not even a consideration.
    # 2. Therefore, this should be a dp problem.
    # 3. The first digit should not be 0.
    # 4. If n == 1, the answer will be 9.
    # 5. If n == 2, the msb should be in range [1,9]
    #               (10, 12), (21, 23), (32, 34), (43, 45), (54, 56), (65, 67), (76, 78), (87, 89), (98, 90)
    #    so the answer is 2 * 9 = 18
    # 6. If n == 3, (101, 109, 121, 123), (210, 212, 232, 234), ..., (987, 989, 901, 909)
    # 7. While it goes in this pattern, every digit in [0,9] should appear at least once.
    # 8. If n < 10, return None.
    # 9. else:
    #       if n == 10, it should follow one of these patterns: (1234567890, 2345678901, 345678901, ..., 9012345678)
    # 10. if n == 11, (12345678901 10987654321)

    # 11. The complexity doesn't reduce if I took this way of approach.
    # 12. Essential requirements:
    #       a. Computing every possible combination cannot be avoided.
    #       b. so tabulation is needed.
    #       c. the point is how I track and store the correct states.
    #       d. dp[length] should be checked.
    #       e. dp[last_digit] also needs to be checked.
    #       f. dp[used_digit] is needed.
    # 13. So it goes something like this: dp[length][last_digit][digits_used]
    # 14. One of the main ideas is how I track the used digits.
    # 15. As it is limited to only 10 digits, bitmasking comes in.
    # 16. While brute-forcing the whole tree in possible way, store which digits have been used so far.
    # 17. When the computation is done, with full_mask 0b1111111111, add the count if state matches.
    # 18. Return count % MOD

    n = int(input())
    print(every_stair_numbers(n))
