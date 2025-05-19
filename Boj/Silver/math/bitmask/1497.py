import sys

input = sys.stdin.readline


def count_bits(x: int) -> int:
    count = 0
    while x:
        x &= x - 1
        count += 1

    return count


def find_min_guitars(n: int, m: int) -> int:
    # TC = O(2^N) = O(2^10) = O(10^3) < 2000ms
    # SC = O(N)

    guitars = []
    for _ in range(n):
        _, playable = input().split()
        bits = 0
        for i, char in enumerate(playable):  # O(M)
            if char == "Y":
                bits |= 1 << ((m - 1) - i)
        guitars.append(bits)

    min_guitars = float("inf")
    max_songs = 0

    for mask in range(1, 1 << n):
        # This outer loop represents the subset of selected guitars.
        # 01001 means guitars[0] and guitars[3] are being selected.

        combined = 0
        count = 0

        for i in range(n):
            # The inner loop checks if each guitar is in the current subset.
            # If so, it compares playable songs of the guitar by bit operation
            #   and records it into "combined".
            # And tracks the count of guitars needed with "count".

            if mask & (1 << i):
                combined |= guitars[i]
                count += 1

        playable_songs = count_bits(combined)
        if playable_songs > max_songs:
            max_songs = playable_songs
            min_guitars = count
        elif playable_songs == max_songs:
            min_guitars = min(min_guitars, count)

    return min_guitars if max_songs > 0 else -1


if __name__ == "__main__":
    # 1. N number of guitars are given.
    # 2. Each guitar can play certain songs:
    #       Y for playable, N for not.
    # 3. For M number of songs, find the minimum number of required guitars,
    #       that can play as many songs as possible.
    # 4. Print -1 if nothing can be played.

    # Constraints
    # TIME 2000ms
    # SPACE 128MB
    # 1. 1 <= N <= 10
    # 2. 1 <= M <= 50
    # 3. 2 <= guitar's name <= 50

    # Approach
    # 1. As the possibility is given as 'YYNNY' format,
    #       it is feasible to apply bitmasking for this problem.
    # 2. Y corresponds for 1, N for 0.
    # 3. Because M ranges to 50, using an integer will exceed 4 bytes.
    # 4. There are two options:
    #       a. using array: O(M^2)
    #       b. using long long in c: O(M)
    # 5. As python doesn't have a size boundary for integer type anyway,
    #       choosing explicit bitmasking will be much desirable.
    # 6. mask = 0
    #   _, playable = input.split()
    #       bits = 0
    #       for i, char in enumerate(playable):
    #           if char == "Y":
    #               bits |= 1 << (M-i)
    #       difference = mask ^ bits
    #       if difference:
    #           min_guitars += 1
    #           mask &= difference
    # 7. This initial approach has a logical issue: all the bits should sort in descending order.
    # 8. Nested loop is unavoidable to correctly determine the minimum number of guitars.

    # a. songs[i] == 1: continue
    # b. not playable[i]: continue
    # c. not songs[i] and playable[i]:
    #       added = True
    #       songs[i] = 1
    #   if added: min_guitars += 1

    n, m = map(int, input().split())
    print(find_min_guitars(n, m))
