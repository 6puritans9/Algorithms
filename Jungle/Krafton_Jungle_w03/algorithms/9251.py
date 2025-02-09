import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_lcs(strings):
    lcs = [[0 for i in range(len(strings[0]) + 1)] for j in range(len(strings[1]) + 1)]
    string_A = strings[1]
    string_B = strings[0]

    for j, letter_B in enumerate(string_B):
        for i, letter_A in enumerate(string_A):
            if letter_A == letter_B:
                lcs[i + 1][j + 1] = 1 + lcs[i][j]
            else:
                lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])
    result = lcs[len(string_A)][len(string_B)]

    return result


if __name__ == "__main__":
    strings = []
    for _ in range(2):
        strings.append(get_input())

    print(get_lcs(strings))
