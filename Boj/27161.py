import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_turn(turn, is_clockwise):
    step = 1
    if not is_clockwise:
        step = -1

    return ((turn + step - 1) % 12) + 1


def play(_symbol, _time, turn, is_clockwise):
    t = get_turn(turn, is_clockwise)

    if _symbol == "HOURGLASS" and _time == t:
        return [t, "NO", is_clockwise]
    elif _symbol == "HOURGLASS":
        return [t, "NO", not is_clockwise]
    elif _time == t:
        return [t, "YES", is_clockwise]
    else:
        return [t, "NO", is_clockwise]



if __name__ == "__main__":
    N = int(get_input())
    instructions = []
    is_clockwise = True
    turn = 0

    for i in range(N):
        instructions.append(get_input().split())

    for instruction in instructions:
        _symbol = instruction[0]
        _time = int(instruction[1])

        result = play(_symbol, _time, turn, is_clockwise)
        turn = result[0]
        is_clockwise = result[2]
        print(f"{result[0]} {result[1]}")
