import sys


def get_input():
    return sys.stdin.readline().rstrip()


def encipher(_str):
    SHIFT = 13
    cipher = ""

    for char in _str:
        # integers and blank space
        if 48 <= ord(char) <= 57 or ord(char) == 32:
            cipher += char
            continue
        # capital letters
        if 65 <= ord(char) <= 90:
            cipher += chr((ord(char) - ord('A') + SHIFT) % 26 + ord('A'))
        else:
            cipher += chr((ord(char) - ord('a') + SHIFT) % 26 + ord('a'))

    return cipher


if __name__ == "__main__":
    _str = get_input()
    print(encipher(_str))
