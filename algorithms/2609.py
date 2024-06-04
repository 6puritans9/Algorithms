import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    numbers = [int(num) for num in get_input().split()]
    small, big = sorted(numbers)
    gcd = None
    lcm = None

    for n in range(small + 1, 0, -1):
        if not small % n and not big % n:
            gcd = n
            break

    n = 1
    while not lcm:
        if not big * n % small:
            lcm = big * n
            break
        n += 1

    print(gcd)
    print(lcm)
