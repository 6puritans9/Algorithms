import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    word = get_input()
    chars = [-1] * 26
    ASCII_VALUE = 97

    for idx, letter in enumerate(word):
        char_idx = ord(letter) - ASCII_VALUE
        if chars[char_idx] == -1:
            chars[char_idx] = idx

    for char in chars:
        if idx == 25:
            print(char)
        else:
            print(char, end=" ")
