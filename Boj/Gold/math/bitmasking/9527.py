import sys

input = sys.stdin.readline


def count_ones(n):
    if n == 0:
        return 0

    result = 0
    length = n.bit_length()

    for i in range(length):
        bit = 1 << i
        total_pairs = (n + 1) // (bit << 1)
        result += total_pairs * bit

        remaining = (n + 1) % (bit << 1)
        result += max(0, remaining - bit)

    return result


if __name__ == "__main__":
    # 1. Two natural numbers a, b are given.
    # 2. For x which ranges in (a <= x <= b),
    # 3. Find the count of 1 that appears
    #    when x was converted into a binary.

    # Constraints
    # TIME 1000ms
    # SPACE 128MB
    # 1. 1 <= A <= B <= 10^16

    # Approach
    # 1. To count every 10^16 number in the worst case,
    #    the given time 1s is definitely insufficient.
    # 2. Every digit in the range can have 2 states.
    # 3. The pattern goes for a fixed digit 1,
    #    that digit will appear n times,
    #    and its children will appear n//2 times.
    #       0010 0011 >> 3
    #       0100 0101 0110 0111 >> 8
    #       1000 1001 1010 1011 1100 >> 10
    # 4. So the logic goes as following:
    #       a. the length of a given number in binary is log_2(a), log_2(b)
    #       b. the count of '1's that appears between A and B can be easily computed as n('length') + (n//2 * n-1)
    #       c. the tricky part is getting the partial '1's.
    # 5. This problem requires a mathematical approach with bit manipulation,
    #       that is out of my capability for me right now.
    # 6. I'll revisit this problem later.

    # 3 to 6
    # 011 >> 1 + 1 = 2
    # 100 101 110 >> 3 + 1 + 1 = 5

    # '1's of 2^2 - '1's of 2^1 = 3 - 1 = 2

    # 010 011
    # 100 101 110 111 >> 4 + 2 + 2 = 8
    # 1000 1001 1010 1011 1100 1101 1110 1111 >> 8 + 4 + 4 + 4 = 20

    # 101 >> 7
    # 110 >> 5

    a, b = map(int, input().split())
    result = count_ones(b) - count_ones(a - 1)
    print(result)
