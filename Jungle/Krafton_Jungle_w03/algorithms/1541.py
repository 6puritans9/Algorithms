import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_result(user_input):
    if user_input.startswith("-"):
        user_input = "0" + user_input

    total = 0
    chunks = user_input.split("-")

    total += sum([int(num) for num in chunks[0].split("+")])
    for chunk in chunks[1:]:
        total -= sum([int(num) for num in chunk.split("+")])

    return total


if __name__ == "__main__":
    user_input = get_input()
    print(get_result(user_input))
