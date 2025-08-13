import sys

input = sys.stdin.readline


def explode(string: list[str], detonator: list[str]) -> list[str]:
    # TC = O(N)
    # SC = O(N)

    stack = []
    len_det = len(detonator)

    for char in string:
        stack.append(char)

        if len(stack) >= len_det and stack[-len_det:] == detonator:
            for _ in range(len_det):
                stack.pop()

    return stack


if __name__ == "__main__":
    # 1. An input string and detonator string is given.
    # 2. If the input contains detonator, all the detonator gets removed.
    # 3. After explosion, the remaining forms a new string.
    # 4. Explosion repeats until there's no detonator in the remaining string.
    # 5. Print the remaining.
    #       if not remaining, print("FRULA")

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= length <= 10^6
    # 2. 1 <= detonator <= 36
    # 3. All the strings consist of alphabet in uppercase or lowercase, and number.

    # Approach
    # 1. Recursive linear search will probably lead to time over. O(10^6 * N)
    # 2. Handle the string like a stream by using stack. O(N)

    string = [char for char in input().rstrip()]
    detonator = [char for char in input().rstrip()]

    remain = explode(string, detonator)
    print("".join(remain) if remain else "FRULA")
