import sys


def get_input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = 9
    combinations = []
    dwarves = []
    for i in range(N):
        dwarves.append(int(get_input()))

    # 0~8
    for i in range(N):
        for j in range(i+1, N):
            combinations.append([i, j])

    total = sum(dwarves)
    result = []
    for combination in combinations:
        if total - dwarves[combination[0]] - dwarves[combination[1]] == 100:
            dwarves.pop(combination[1])
            dwarves.pop(combination[0])
            break

    for dwarf in dwarves:
        print(dwarf)
