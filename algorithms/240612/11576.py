import sys
from collections import deque

print = sys.stdout.write


def convert_to_decimal(numbers, base, place_values):
    result = 0

    for i, number in enumerate(numbers):
        result += number * (base ** (place_values - (i + 1)))

    return result


def convert_to_dst_base(deci, dst_base):
    result = deque()

    while deci > 0:
        remainder = deci % dst_base
        deci //= dst_base
        result.appendleft(str(remainder))

    return result


if __name__ == "__main__":
    src_base, dst_base = [int(num) for num in input().split()]
    place_values = int(input())
    numbers = [int(num) for num in input().split()]

    deci = convert_to_decimal(numbers, src_base, place_values)
    result = convert_to_dst_base(deci, dst_base)

    print(" ".join(result))
