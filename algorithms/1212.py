import sys

print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = get_input()

    deci = int(N, 8)
    binary = bin(deci)[2:]

    print(binary)

    # The snippet below gets timed out
    #
    # if deci == 0:
    #     print("0")
    # else:
    #     binary = deque()
    #     while deci > 0:
    #         remain = deci % 2
    #         deci //= 2
    #         binary.appendleft(str(remain))
    #
    #     print("".join(binary))
