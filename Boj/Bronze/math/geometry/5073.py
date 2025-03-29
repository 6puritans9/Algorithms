import sys

input = sys.stdin.readline


def print_category(a: int, b: int, c: int) -> None:
    # TC = O(N) == (3/8 * 10^3)ms
    # SC = O(1)

    category = ["Invalid", "Equilateral", "Isosceles", "Scalene"]

    if not (a + b > c and b + c > a and c + a > b):
        print(category[0])
    elif a == b == c:
        print(category[1])
    elif a == b or b == c or c == a:
        print(category[2])
    else:
        print(category[3])


if __name__ == "__main__":
    # Problem
    # Length of three sides which consists a triangle is given
    # There are four cases to form a triangle
    #   1. Equilateral : 3 same
    #   2. Isosceles : 2 same, 1 different
    #   3. Scalene : 3 different, form a valid triangle
    #   4. Invalid : else
    # "0 0 0" marks the end of input
    # Print the corresponding category for each input

    # Constraint
    # Time 1000ms
    # Space 128MB
    # 1 <= n <= 10^3

    # Approach
    # 1. Determine the category for O(4)
    #   - if not(a+b>c and b+c>a and c+a>b) => invalid
    #   - elif a==b and b==c and c==a => e
    #   - elif (a==b and b!=c) or (b==c and c!=a) or (c==a and a!=b) => i
    #   - else => s
    # 2. Print the result on the fly
    # 3. Terminate the process on "0 0 0"

    while True:
        a, b, c = map(int, input().split())
        if not a and not b and not c:
            break

        print_category(a, b, c)
