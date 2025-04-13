import sys
from collections import deque

input = sys.stdin.readline


class Prog:
    def __init__(self):
        self.p = [char for char in input().rstrip()]
        self.n = int(input())
        self.integers = deque(input().rstrip()[1:-1].split(","))

    def is_valid(self, arr: deque[int], instruction: str) -> bool:
        if self.n != len(arr):
            return False

        if instruction == 'D' and not self.n:
            return False

        return True

    def run(self) -> deque[int] or None:
        arr = self.integers
        is_reversed = False

        for instruction in self.p:
            if not self.is_valid(arr, instruction):
                return None

            if instruction == 'R':
                is_reversed = not is_reversed

            else:
                self.d(arr, is_reversed)

        if is_reversed:
            arr = self.r(arr)

        return arr

    def r(self, arr: deque[int]) -> deque[int]:
        # TC = O(N)
        # SC = O(N) = O(10^5) = 4bytes * 10^5 = 400KB

        new_arr = deque()

        for element in arr:
            new_arr.appendleft(element)

        return new_arr

    def d(self, arr: deque[int], reversed: bool) -> None:
        # TC = O(1)
        # SC = O(1)

        if not reversed:
            arr.popleft()
        else:
            arr.pop()
        self.n -= 1


if __name__ == "__main__":
    # 1. For given tests,
    # there are function R and D.
    # 2. R reverses its input list,
    # D drops the first element of its input and returns the rest,
    # or gives an error if input is empty.
    # 3. 'AB' applies function 'A' to its input then function 'B' to the resulting list.
    # 4. The program interpreter might ask to write a new function.

    # Constraints
    # TIME 1000ms
    # SPACE 256MB
    # 1. 1 <= length(p) <= 10^5
    # 2. 0 <= n <= 10^5
    # 3. 1 <= xi <= 10^2

    # Approach
    # 1. Make a class to instantiate for each case
    # 2. Create a new function that checks the validity

    tests = int(input())
    for _ in range(tests):
        p = Prog()
        result = p.run()

        if result is None:
            print("error")
            continue

        output = "["
        output += ",".join(str(x) for x in result)
        output += "]"
        print(output)
