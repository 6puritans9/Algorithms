import sys

input = sys.stdin.readline


def find_total_length(n: int) -> int:
    # TC = O(1)
    # SC = O(1)

    total_length = (3 * n) + n

    return total_length


if __name__ == "__main__":
    # Problem
    # For given N, there is a pyramid which has N height
    # Each line goes in this pattern: 1, 1+1, 1+1+1, 1+1+1+1+1, ...
    # find the length of outside lines that these blocks make

    # Constraints
    # 1<= n <= 10^9
    # Time 1000ms
    # Space 512MB

    # Approach
    # 1. Each line has sidelines length of 2
    # 2. Also, each one has top length 1
    # 3. THe only thing changes is the bottom line
    # 4. It goes along with the height N
    # 5. The only pain point is that the N exceeds 10^8, which leads to time over
    # 6. So the solution should take O(1) not O(N)

    n = int(input())
    print(find_total_length(n))
