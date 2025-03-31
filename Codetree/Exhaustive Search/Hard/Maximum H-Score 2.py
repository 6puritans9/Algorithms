def greedy_max_h_index(n: int, l: int, citations: list[int]) -> int:
    # TC = O(100 * N) = O(10^2 * 10^2) == 500ms
    # SC = O(1)

    MAX_INDEX = 100

    max_h_index = 0
    for i in range(1, MAX_INDEX + 1):
        h_index = 0
        added = 0

        for citation in citations:
            if citation >= i:
                h_index += 1
            elif citation + 1 >= i and added < l:
                h_index += 1
                added += 1

        if h_index >= i:
            max_h_index = i

    return max_h_index


if __name__ == "__main__":
    # Problem
    # For given N numbers,
    # add 1 to each L element
    # to maximize H.
    # This prolem asks h-index with a tweak,
    # which can easily be solved in counting sort in O(NK)

    # Constraints
    # 1 <= N <= 10^2
    # 0 <= L <= N
    # 0 <= element <= 10^2
    # Time 5000ms
    # Space 288 MiB

    # Approach
    # 1. I can get h-index for O(NK)
    #   which will increase to O(N * C(N,1)) = O(N * (N!/(L! * (N-1)!)))
    #   that I cannot solve in given time.
    # 2. This will occupy O(100) in memory, which is easily manageable in space though

    # 3. Since the problem only allows to add 1 if possible, this can be solved in greedy approach
    # 4. for i in range(10^2 + 1), find the maximum i, which will be the largest h-index possible
    # 5. for each i, iterate in given numbers, or rather citations,
    # 6. check if +1 can make the valid cases, up to l
    # 7. return max_h_index

    n, l = map(int, input().split())
    citations = [int(num) for num in input().split()]

    print(greedy_max_h_index(n, l, citations))

# An exponential time solution below:
#
# def get_h_index(n: int, numbers: list[int]) -> int:
#     arr = [0 for _ in range(n + 1)]
#     for number in numbers:
#         arr[number] += 1
#
#     papers = 0
#     for h_index in range(n, -1, -1):
#         if papers >= h_index:
#             return h_index
#         papers += arr[h_index]
#
#     return 0
#
#
# def increase_l_elements(n, l, numbers, start, count):
#     if count >= l:
#         return get_h_index(n, numbers)
#     if start == n:
#         return 0
#
#     max_h = 0
#
#     for i in range(start, n):
#         numbers[i] += 1
#         max_h = max(max_h, increase_l_elements(n, l, numbers, i + 1, count + 1))
#         numbers[i] -= 1
#     max_h = max(max_h, increase_l_elements(n, l, numbers, start + 1, count))
#
#     return max_h
#
#
# def find_max_h(n: int, l: int, numbers: list[int]) -> int:
#     return increase_l_elements(n, l, numbers, 0, 1)
#
#
# if __name__ == "__main__":
#     # Problem
#     # For given N numbers,
#     # add 1 to each L element
#     # to maximize H.
#     # This prolem asks h-index with a tweak,
#     # which can easily be solved in counting sort in O(NK)
#
#     # Constraints
#     # 1 <= N <= 10^2
#     # 0 <= L <= N
#     # 0 <= element <= 10^2
#     # Time 5000ms
#     # Space 288 MiB
#
#     # Approach
#     # 1. I can get h-index for O(NK)
#     #   which will increase to O(NK * nCl) == O(10^4 * 10^4) = 8/8 * 10^3ms
#     # 2. This will occupy O(100) in space, which is easily manageable
#
#     # 3. Add 1 for L selected elements in nCl combination
#     # 4. assign a counting sort array
#     # 5. compare each result to find max_h
#     # 6. return max_h
#
#     n, l = map(int, input().split())
#     numbers = [int(num) for num in input().split()]
#
#     print(find_max_h(n, l, numbers))
