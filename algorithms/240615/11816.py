import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = get_input()
    deci = None


    if N[1] == "x":
        deci = int(N, 16)
    elif N[0] == "0":
        deci = int(N, 8)
    else:
        deci = int(N, 10)

    print(deci)