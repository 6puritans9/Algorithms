import sys
print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def get_primes(limit):
    prime_table = [1] * limit
    prime_table[0] = prime_table[1] = 0

    for i in range(2, limit):
        if i * i > limit:
            break

        if prime_table[i]:
            for j in range(i*i, limit, i):
                prime_table[j] = 0

    return prime_table


def get_result(primes, limit, num):
    result = []

    for i in range(2, limit):
        if num <= 1:
            break

        if primes[i]:
            while num % i == 0:
                result.append(str(i))
                num //= i

    return result


if __name__ == "__main__":
    N = int(get_input())
    LIMIT = 10000001
    primes = get_primes(LIMIT)
    result = get_result(primes, LIMIT, N)

    print("\n".join(result))
