import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_prime(limit):
    primes = [1] * (limit + 1)
    primes[0] = primes[1] = 0

    for i in range(2, limit + 1):
        if i * i > limit:
            break

        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = 0

    return primes


def get_answer(_input, prime_table):
    LENGTH = 10001
    for i, prime in enumerate(prime_table):
        if i > LENGTH:
            return False

        if prime:
            if not prime_table[_input - i]:
                continue
            return [i, _input - i]


if __name__ == "__main__":
    N = 1000000
    prime_table = get_prime(N)

    inputs = []
    _input = 1

    while _input:
        _input = int(get_input())
        if _input:
            inputs.append(_input)

    for _input in inputs:
        answer = get_answer(_input, prime_table)
        if not answer:
            print("Goldbach's conjecture is wrong.")
        else:
            print(f"{_input} = {answer[0]} + {answer[1]}")
