def can_partition(n:int, m:int, numbers:list[int], max_sum:int) -> bool:
    # TC = O(N)
    # SC = O(1)

    cur_sum = 0
    partitions = 1

    for num in numbers:
        if num > max_sum:
            return False

        if cur_sum + num > max_sum:
            partitions += 1
            cur_sum = num
            if partitions > m:
                return False
        else:
            cur_sum += num

    return True


def find_minimized_max_subset_sum(n: int, m: int, numbers: list[int]) -> int:
    # TC = O(log(sum(numbers))
    # SC = O(1)

    low, high = max(numbers), sum(numbers)
    best_max_sum = high

    while low <= high:
        mid = (low + high) // 2

        if can_partition(n, m, numbers, mid):
            best_max_sum = mid
            high = mid - 1
        else:
            low = mid + 1

    return best_max_sum


if __name__ == "__main__":
    # Problem
    # Among given N numbers, place (M-1) partitions
    # to make the largest sum of each subset to be minimized

    # Constraints
    # 2 <= M <= N <= 10^2
    # 1 <= number <= 10^2
    # Time 5000ms
    # Space 288 MiB

    # Approach
    # 1. This one could be solved with backtracking
    # 2. Make combinations (n-1)C(m-1)
    # 3. Find the smallest sum of each combination
    # 4. Return and Print
    # 5. But backtracking approach has proven to be quite verbose,
    # 6. Binary search would be an ideal solution
    # TC = O(N log(sum(numbers))
    # SC = O(1)

    n, m = map(int, input().split())
    numbers = [int(num) for num in input().split()]

    print(find_minimized_max_subset_sum(n, m, numbers))
