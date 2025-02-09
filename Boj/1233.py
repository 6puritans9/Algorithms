def get_sums(facets):
    S1, S2, S3 = facets
    combination_sums = [0] * ((S1 * S2 * S3) + 1)
    max_sum = 0
    max_sum_count = 0

    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                _sum = i + j + k

                combination_sums[_sum] += 1
                if combination_sums[_sum] > max_sum_count:
                    max_sum_count = combination_sums[_sum]
                    max_sum = _sum

    return max_sum


if __name__ == "__main__":
    facets = [int(num) for num in input().split()]

    print(get_sums(facets))
