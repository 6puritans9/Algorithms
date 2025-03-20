from collections import deque


# Total TC = O(N * M)
# Total SC = O(M)


def compare(m: int, seq_b: list[int], subarr: list[int]) -> bool:
    # TC = O(M)
    # SC = O(M)

    freq = {}
    for target in seq_b:
        freq[target] = freq.get(target, 0) + 1

    for number in subarr:
        if number in freq and freq[number] > 0:
            freq[number] -= 1
            continue

        return False

    return True


def find_matching_counts(n: int, m: int, seq_a: list[int], seq_b: list[int]) -> int:
    # TC = O(N)
    # SC = O(M)

    counts = 0
    subarr = deque()

    left = 0
    for right in range(n):
        subarr.append(seq_a[right])

        if right - left > m - 1:
            subarr.popleft()
            left += 1

        if right - left == m - 1:
            counts += 1 if compare(m, seq_b, subarr) else 0

    return counts


if __name__ == "__main__":
    # Problem:
    # Two sequences are given:
    # Seq A consists of N numbers
    # Seq B consists of M numbers
    # Find continuous subarrays of seq A, which includes elements of seq B

    # Constraints:
    # 1 <= N, M <= 100
    # 1 <= element <= 100

    # Approach:
    # 1. Form subarrays of A with sliding window O(N)
    # 2. If len(subarr) == M:
    #       compare each element with B
    #       using hashmap O(M)
    # 3. count += 1 if it matches

    n, m = map(int, input().split())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]

    print(find_matching_counts(n, m, a, b))
