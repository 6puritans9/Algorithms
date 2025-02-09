import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    binary = get_input()
    deci = 0

    for bit in binary:
        deci = (deci << 1) | int(bit)

    if deci == 0:
        octal = "0"
    else:
        octal = ""
        while deci > 0:
            remain = deci % 8
            deci = deci // 8
            octal = str(remain) + octal

    print(octal)
