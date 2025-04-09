import sys

input = sys.stdin.readline


def find_visit_order(n: int, row: int, col: int) -> int:
    # TC = O(logN)
    # SC = O(1)

    order = 0
    size = 2 ** n

    while size > 1:
        half = size // 2
        cells_per_quadrant = half * half  # square

        # top-left
        if row < half and col < half:
            pass
        # top-right
        elif row < half and col >= half:
            order += cells_per_quadrant
            col -= half
        # bottom-left
        elif row >= half and col < half:
            order += 2 * cells_per_quadrant
            row -= half
        # bottom-right
        else:
            order += 3 * cells_per_quadrant
            row -= half
            col -= half

        size //= 2

    return order


if __name__ == "__main__":
    # For a 2^n * 2^n grid,
    # the traversal path forms a 'Z' figure in recursive fashion.
    # For given N,
    # Find out the sequential order of visiting (r,c)

    # Constraints
    # TIME 500ms
    # SPACE 512MB
    # 1 <= N <= 15
    # 0 <= r, c < 2^n

    # Approach
    # 1. Because of the tight time window, naive recursion is not feasible
    # 2. Divide and conquer will solve this in O(logN) = O(15) = O(1)
    # 3. Start from dividing the grid into 4 quadrants
    # 4. if row < size//2 && col < size//2:
    #       top-left
    #    elif row < size//2 && col >= size//2:
    #       top-right
    #    elif row >=size//2 && col < size//2:
    #       bottom-left
    #    else:
    #       bottom-right
    # 5. Make a transition to the corresponding quadrant
    # 6. repeat

    n, r, c = map(int, input().split())
    print(find_visit_order(n, r, c))
