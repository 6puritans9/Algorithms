import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    word = [char for char in get_input()]
    counts = [0] * 26

    for char in word:
            idx = ord(char) - 97
            counts[idx] += 1

    for count in counts:
        print(count, end=" ")
