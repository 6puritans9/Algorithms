import sys

print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def get_prime(big):
    bits = [1] * (big + 1)
    bits[0] = bits[1] = 0

    for i in range(2, big):
        if (i * i) > big:
            break

        if bits[i]:
            for j in range(i * i, big + 1, i):
                bits[j] = 0

    return bits


if __name__ == "__main__":
    numbers = [int(num) for num in get_input().split()]
    small, big = numbers

    primes = get_prime(big)
    for i in range(small, big + 1):
        if primes[i]:
            print(f"{i}\n")
