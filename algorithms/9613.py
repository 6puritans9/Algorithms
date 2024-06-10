def get_gcd(length, numbers):
    gcd_sum = 0

    for i in range(length):
        for j in range(i+1, length):
            big = max(numbers[i], numbers[j])
            gcd = min(numbers[i], numbers[j])

            while big % gcd:
                temp = big
                big = gcd
                gcd = temp % gcd

                if not gcd:
                    gcd_sum += 1
                    break
            gcd_sum += gcd

    return gcd_sum


if __name__ == "__main__":
    N = int(input())
    # numbers = []
    result = []

    for _ in range(N):
        numbers = [int(num) for num in input().split()]
        result.append(get_gcd(numbers[0], numbers[1:]))

    for num in result:
        print(num)
