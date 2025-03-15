# This one asks to make combinations which length is 7 and sum is 100,
# which can be solved with backtracking.

def backtrack(n: int, dwarves: list[int], start: int, cur_list: list[int]) -> list[int]:
    if len(cur_list) == 7 and sum(cur_list) == 100:
        return cur_list

    for i in range(start, n):
        cur_list.append(dwarves[i])
        result = backtrack(n, dwarves, i + 1, cur_list)
        if result:
            return result
        cur_list.pop()

    return []


def find_seven(dwarves: list[int]) -> list[int]:
    return backtrack(9, dwarves, 0, [])


if __name__ == "__main__":
    dwarves = [int(input()) for _ in range(9)]

    for dwarf in sorted(find_seven(dwarves)):
        print(dwarf)
