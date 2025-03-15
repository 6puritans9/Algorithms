def count_factor_x(value, x):
    count = 0
    while value > 0:
        count += value // x
        value //= x

    return count


def count_5(n, m):
    count_n = count_factor_x(n, 5)
    count_m = count_factor_x(m, 5)
    count_n_minus_m = count_factor_x(n-m, 5)

    return count_n-(count_m + count_n_minus_m)


def count_2(n,m):
    count_n = count_factor_x(n, 2)
    count_m = count_factor_x(m, 2)
    count_n_minus_m = count_factor_x(n - m, 2)

    return count_n - (count_m + count_n_minus_m)


if __name__ == "__main__":
    n, m = [int(num) for num in input().split()]

    count_5 = count_5(n, m)
    count_2 = count_2(n, m)

    print(min(count_5, count_2))
