import sys
# print = sys.stdout.write


def get_input():
    return sys.stdin.readline().rstrip()


def get_lcm(numbers):
    lcm = None
    small, big = sorted(numbers)

    n = 1
    while n:
        if not big * n % small:
            lcm = big * n
            break
        n += 1

    return lcm



if __name__ == "__main__":
    N = int(get_input())
    numbers = []

    for i in range(N):
        _input = [int(num) for num in get_input().split()]
        numbers.append(_input)

    for sub_list in numbers:
        print(get_lcm(sub_list))
