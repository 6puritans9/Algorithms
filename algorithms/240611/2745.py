import sys
print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def convert(N, B):
    base = int(B)
    length = len(N)

    if base <= 10:
        return int(N, base)

    result = 0
    for i in range(length):
        if 48 <= ord(N[i]) <= 57:
            result += int(N[i], 10) * (base ** (length - i - 1))
        else:
            value = ord(N[i]) - 55
            result += value * (base ** (length - i - 1))

    return result


if __name__ == "__main__":
    N, B = [_str for _str in get_input().split()]
    result = convert(N, B)
    print(str(result))
